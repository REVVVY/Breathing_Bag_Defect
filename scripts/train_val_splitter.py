import json
import random

# Load the original JSON file
with open('C:\\Breathing_Bag_Defect\\Mask_RCNN\\Dataset_manual\\output_annotations.json') as f:
    annotations = json.load(f)

# Get a list of image IDs
image_ids = list(annotations.keys())

# Shuffle the list
random.shuffle(image_ids)

# Split the list into training and validation sets
split_idx = int(0.8 * len(image_ids))
train_ids = image_ids[:split_idx]
val_ids = image_ids[split_idx:]

# Create the new annotation files
train_annotations = {}
val_annotations = {}

# Copy the annotations for each image ID to the appropriate file
for image_id in train_ids:
    train_annotations[image_id] = annotations[image_id]
for image_id in val_ids:
    val_annotations[image_id] = annotations[image_id]

# Save the new annotation files
with open('Dataset_manual\\train.json', 'w') as f:
    json.dump(train_annotations, f)

with open('Dataset_manual\\val.json', 'w') as f:
    json.dump(val_annotations, f)
