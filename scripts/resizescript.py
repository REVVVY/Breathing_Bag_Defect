import os
import sys
import cv2
from mrcnn import utils

inputpath = os.path.join(os.getcwd(), "Dataset_new", "All-Defects")
outputpath = os.path.join(os.getcwd(), "Dataset_new/resize")

if not os.path.exists(outputpath):
    os.makedirs(outputpath)

imagelist = os.listdir(inputpath)
#print(os.listdir(inputpath))

for image in imagelist:
    img = cv2.imread(os.path.join(inputpath, image))
    resized_image, window, scale, padding, crop = utils.resize_image(img, 800, 1024, 0, "square")
    #print(resizeimg)
    cv2.imwrite(os.path.join(outputpath, image), resized_image)

