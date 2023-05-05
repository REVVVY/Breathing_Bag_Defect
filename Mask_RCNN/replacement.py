import re

with open('C:\\Breathing_Bag_Defect\\Mask_RCNN\\temp\\New_Generated.txt', 'r') as f:
    text = f.read()

for i in range(750):
    old_str = f"im_{i}"
    new_str = f"imnew_{i}"
    text = text.replace(old_str, new_str)

with open('new_textfile.txt', 'w') as f:
    f.write(text)