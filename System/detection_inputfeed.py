import cv2
import os
import matplotlib.pyplot as plt
import datetime

input_dir = r'Den här datorn\Redmi Note 11 Pro 5G\Delat internt lagringsutrymme\DCIM\Camera\IMG_20221229_171134.jpg'

img = cv2.imread(input_dir)
cv2.imshow("kukbajs", img)
cv2.waitKey(0)


"""
# Define the paths for input and output directories

output_dir = 'path/to/output/directory'
archive_dir = 'path/to/archive/directory'
batch_size = 9

while True:
    # Check if there is a new folder with images
    for foldername in os.listdir(input_dir):
        folderpath = os.path.join(input_dir, foldername)
        if os.path.isdir(folderpath):
            # Create a new directory for the processed images
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            output_foldername = f"{foldername}_{timestamp}"
            output_folderpath = os.path.join(output_dir, output_foldername)
            os.makedirs(output_folderpath)

            # Process the images in batches
            file_list = os.listdir(folderpath)
            for i in range(0, len(file_list), batch_size):
                batch = file_list[i:i + batch_size]
                processed_images = []
                for filename in batch:
                    if filename.endswith('.jpg') or filename.endswith('.png'):
                        # Read the image from the input directory
                        img = cv2.imread(os.path.join(folderpath, filename))

                        # Apply color enhancement
                        b, g, r = cv2.split(img)
                        # Manipulate the color channels as needed
                        enhanced_img = cv2.merge((b, g, r))

                        # Add the processed image to the list
                        processed_images.append(enhanced_img)

                # Concatenate the processed images horizontally
                img_concatenated = cv2.hconcat(processed_images)

                # Save the processed image to the output directory
                output_filename = f"{filename[:-4]}_processed.png"
                output_filepath = os.path.join(output_folderpath, output_filename)
                cv2.imwrite(output_filepath, img_concatenated)

                # Move the original file to the processed folder
                os.rename(os.path.join(folderpath, filename), os.path.join(output_folderpath, filename))

            # Move the original folder to the archive folder
            os.rename(folderpath, os.path.join(archive_dir, foldername))
"""