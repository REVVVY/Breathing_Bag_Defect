import os
import json
import shutil

# Path to the training and validation JSON files
TRAIN_JSON_PATH = "C:\\Breathing_Bag_Defect\\Mask_RCNN\\Dataset_gen\\train.json"
VAL_JSON_PATH = "C:\\Breathing_Bag_Defect\\Mask_RCNN\\Dataset_gen\\val.json"

# Path to the directory where the images should be moved
TRAIN_DIR = "C:\\Breathing_Bag_Defect\\Mask_RCNN\\Dataset_gen\\train"
VAL_DIR = "C:\\Breathing_Bag_Defect\\Mask_RCNN\\Dataset_gen\\val"

# Make the new directories if they don't already exist
os.makedirs(TRAIN_DIR, exist_ok=True)
os.makedirs(VAL_DIR, exist_ok=True)

# Load the training JSON file
with open(TRAIN_JSON_PATH, "r") as train_file:
    train_data = json.load(train_file)

# Move the training images to the new directory
for img_name in train_data.keys():
    filename = train_data[img_name]["filename"]
    src_path = os.path.join(os.path.dirname(TRAIN_JSON_PATH), filename)
    dst_path = os.path.join(TRAIN_DIR, filename)
    shutil.move(src_path, dst_path)

# Load the validation JSON file
with open(VAL_JSON_PATH, "r") as val_file:
    val_data = json.load(val_file)

# Move the validation images to the new directory
for img_name in val_data.keys():
    filename = val_data[img_name]["filename"]
    src_path = os.path.join(os.path.dirname(VAL_JSON_PATH), filename)
    dst_path = os.path.join(VAL_DIR, filename)
    shutil.move(src_path, dst_path)
