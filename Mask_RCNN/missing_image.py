import os

folder_path = "C:\Breathing_Bag_Defect\Mask_RCNN\object20230509T1215_30"  # Replace with the path to your folder

existing_numbers = set()

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".png") and filename.startswith("image_"):
        try:
            number = int(filename.split("_")[1].split(".")[0])
            existing_numbers.add(number)
        except ValueError:
            pass

# Find the missing numbers
missing_numbers = sorted(set(range(350)) - existing_numbers)

print("Missing numbers:", missing_numbers)
