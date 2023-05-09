import os
import json

# Folder path containing images
folder_path = 'C:/Breathing_Bag_Defect/Mask_RCNN/Dataset_lab/Add'

# JSON annotation file path
annotation_file_path = os.path.join(folder_path, 'dataset.json')

# Output annotation file path
output_file = 'output_annotations.json'

images = []

# Loop through the files in the folder
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        if filename.lower().endswith('.jpg'):
            # Append the file name to the array
            sizeinbyte = os.path.getsize(os.path.join(folder_path, filename))
            temp = filename + str(sizeinbyte)
            images.append(temp)
    
# Print the file names
#print(images)


# Load the JSON annotation file
with open(annotation_file_path) as file:
    annotation_data = json.load(file)

ann_ids = list(annotation_data.keys())
#print(image_ids)

# Dictionary to store extracted annotations
annotations = {}

num = 0

for an_id in ann_ids:
    for img_id in images:
        #print(img_id)
        #print(an_id)
        if an_id == img_id:
            annotations[img_id] = annotation_data[an_id]

#print(annotations)

# Save the extracted annotations to the output file
with open(output_file, 'w') as file:
    json.dump(annotations, file, indent=4)

