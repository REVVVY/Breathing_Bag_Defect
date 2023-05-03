import os
import sys
import argparse

import numpy as np
import json

import cv2
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import skimage.draw

from mrcnn.config import Config
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize

class CustomConfig(Config):
    """Configuration for training on the custom  dataset.
    Derives from the base Config class and overrides some values.
    """
    # Give the configuration a recognizable name
    NAME = "object"

    # We use a GPU with 12GB memory, which can fit two images.
    # Adjust down if you use a smaller GPU.
    IMAGES_PER_GPU = 1

    # Number of classes (including background)
    NUM_CLASSES = 1 + 1  # Background + Hole  # car and truck

    RPN_ANCHOR_SCALES = (4, 8, 16, 32, 64)  # anchor side in pixels
    
    LEARNING_RATE = 0.001
    
    # Number of validation steps to run at the end of every training epoch.
    # A bigger number improves accuracy of validation stats, but slows
    # down the training.
    VALIDATION_STEPS = 50
    
    # Non-maximum suppression threshold for detection
    DETECTION_NMS_THRESHOLD = 0.001

    USE_MINI_MASK = False # True from start, try False to calc mAP see discord
    # Number of training steps per epoch
    STEPS_PER_EPOCH = 2000

    # Skip detections with < 90% confidence
    DETECTION_MIN_CONFIDENCE = 0.5

# Code for Customdataset class. Same code is present in custom.py file also
class CustomDataset(utils.Dataset):

    def load_custom(self, dataset_dir, subset):

        self.add_class("object", 1, "Hole")
        #self.add_class("object", 2, "Discoloration")

        assert subset in ["train", "val"]
        dataset_dir = os.path.join(dataset_dir, subset)
        annotations1 = json.load(open('C:\Breathing_Bag_Defect\Mask_RCNN\Dataset\\' + subset + '\\dataset.json'))

        annotations = list(annotations1.values())  # don't need the dict keys

        annotations = [a for a in annotations if a['regions']]
        
        # Add images
        for a in annotations:
           
            polygons = [r['shape_attributes'] for r in a['regions']] 
            objects = [s['region_attributes']['names'] for s in a['regions']]
            #print("objects:",objects)
            name_dict = {"Hole": 1}  # Lägg komma efteråt följt av nästa klass vid flera
            num_ids = [name_dict[a] for a in objects]

            #print("numids",num_ids)
            image_path = os.path.join(dataset_dir, a['filename'])
            image = skimage.io.imread(image_path)
            height, width = image.shape[:2]

            self.add_image(
                "object", 
                image_id=a['filename'],  # use file name as a unique image id
                path=image_path,
                width=width, height=height,
                polygons=polygons,
                num_ids=num_ids
                )

    def load_mask(self, image_id):
       
        image_info = self.image_info[image_id]
        if image_info["source"] != "object":
            return super(self.__class__, self).load_mask(image_id)

        info = self.image_info[image_id]
        if info["source"] != "object":
            return super(self.__class__, self).load_mask(image_id)
        num_ids = info['num_ids']
        mask = np.zeros([info["height"], info["width"], len(info["polygons"])],
                        dtype=np.uint8)
        for i, p in enumerate(info["polygons"]):

            rr, cc = skimage.draw.polygon(p['all_points_y'], p['all_points_x'])

            mask[rr, cc, i] = 1

        num_ids = np.array(num_ids, dtype=np.int32)
        return mask, num_ids #np.ones([mask.shape[-1]], dtype=np.int32)

    def image_reference(self, image_id):
        """Return the path of the image."""
        info = self.image_info[image_id]
        if info["source"] == "object":
            return info["path"]
        else:
            super(self.__class__, self).image_reference(image_id)


model_dir = ""
weight_path = "C:\\Breathing_Bag_Defect\\weights\\object20230427T1027\\mask_rcnn_object_0030.h5"
dataset_dir = "C:\\Breathing_Bag_Defect\\Mask_RCNN\\Dataset"
image_directory = "C:\\Breathing_Bag_Defect\\Mask_RCNN\\Dataset\\val"

model = modellib.MaskRCNN(mode="inference", model_dir=model_dir, config=CustomConfig())
print("Loading weights ", weight_path)
model.load_weights(weight_path, by_name=True)

# input_image = "C:\\Breathing_Bag_Defect\\Mask_RCNN\\Dataset\\val\\im_12.jpg"

# raw_image = cv2.imread(input_image)
# raw_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)

def load_image(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


image_files = os.listdir(image_directory)
image_files.sort()
image_paths = [os.path.abspath(os.path.join(image_directory, x)) for x in image_files]
image_paths = list(filter(lambda x: os.path.splitext(x)[1].lower() == ".jpg", image_paths))

dataset = CustomDataset()
dataset.load_custom(dataset_dir, "val")
dataset.prepare()

def predict(img, ax):
    results = model.detect([img], verbose=1)
    visualize.display_instances(img, results[0]['rois'], results[0]['masks'], results[0]['class_ids'], 
                                dataset.class_names, results[0]['scores'], ax=ax)


fig, (img_in, img_pr) = plt.subplots(1, 2)

current_idx = 0
current_image = load_image(image_paths[current_idx])
fig.canvas.manager.set_window_title(f"image {current_idx + 1}/{len(image_paths)}")

img_in.imshow(current_image)
img_in.set_title(f"Original Image: {os.path.basename(image_paths[current_idx])}")
img_in.set_xticks([])
img_in.set_yticks([])

predict(current_image, img_pr)
img_pr.set_title("Predicted Image")
img_pr.set_xticks([])
img_pr.set_yticks([])

# define function for updating image
def update_image():
    img_in.set_title(f"Original Image: {os.path.basename(image_paths[current_idx])}")

    fig.canvas.manager.set_window_title(f"image {current_idx + 1}/{len(image_paths)}")
    current_image = load_image(image_paths[current_idx])
    img_in.imshow(current_image)

    predict(current_image, img_pr)
    img_pr.set_title(f"image: {current_idx + 1}/{len(image_paths)}")

    fig.canvas.draw()

def next_ev(event):
    global current_idx
    current_idx = (current_idx + 1) % len(image_paths)
    update_image()

def prev_ev(event):
    global current_idx
    current_idx = (current_idx + len(image_paths) - 1) % len(image_paths)
    update_image()

# create "next" button and connect to update function
ax_next = plt.axes([0.8, 0.05, 0.1, 0.075])
button_next = Button(ax_next, 'Next')
button_next.on_clicked(update_image)

axprev = fig.add_axes([0.7, 0.05, 0.1, 0.075])
axnext = fig.add_axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(next_ev)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(prev_ev)

plt.show()