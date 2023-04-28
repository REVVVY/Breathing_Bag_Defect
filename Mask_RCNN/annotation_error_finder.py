import json
import os

annotations_file = "C:/Breathing_Bag_Defect/Mask_RCNN/Datasettest/val/dataset.json"

with open(annotations_file, "r") as f:
    data = json.load(f)

for img_id, img_data in data.items():
    filename = img_data["filename"]
    for region in img_data["regions"]:
        region_attributes = region["region_attributes"]
        if "names" not in region_attributes:
            print(f"Error found in {filename}")
