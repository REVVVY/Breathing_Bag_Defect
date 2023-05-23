from PIL import Image, ImageDraw
import json
import os
import random

# Open and load defective image and correct sample to paste defect onto
img_defect = Image.open('C:\\Users\\Johan\\PycharmProjects\\Mask_RCNN_demo\\dataset1\\bot_reg\\defect9.jpg')
img_nondefect = Image.open('C:\\Users\\Johan\\PycharmProjects\\Mask_RCNN_demo\\dataset1\\bot_reg\\non_defect9.jpg')

# Define the polygon for the defect region to copy and paste
# Image cordinates of defect
poly1 = [(1105, 2538), (1110, 2537), (1115, 2537), (1117, 2539), (1113, 2541), (1109, 2543), (1106, 2543), (1104, 2541)]

# Copy the region of interest
#1 Creates mask (black and white) with the same size as the image (resulting in a black image)
#2 Creates a draw object in order to draw lines, rectangles, polygons etc on mask
#3 Fills the polygon on the mask with color white
#4 Creates a copy of img_defect to not modify the original image
#5 Extracts all pixel values from the defect copy and extracts only the mask region
mask = Image.new('1', img_defect.size)
draw = ImageDraw.Draw(mask)
draw.polygon(poly1, fill=1)
cropped_region = img_defect.copy()
cropped_region.putalpha(mask)

# Paste cropped region onto the non-defect image at selected x and y cordinates and saves the image to selected path.
# 1st parameter is the region that is suppost to get added onto the image,
# 2nd parameter is coordinates,
# 3rd is the mask, in this case the region because the transparancy is determinated by the alpha channel of cropped_region
all_pointsx = []
all_pointsy = []

"""
#TESTING IF THE HOLE CAN BE SEEN ON BALLOON
img_new = img_nondefect.copy()
img_new.paste(cropped_region, (730, -1400), cropped_region)
filename = "C:\\Users\\Johan\\PycharmProjects\\Mask_RCNN_demo\\dataset1\\bot_reg\\generated.jpg"
img_new.save(filename)
# x = -100 till 730        , y = -1400 till -750
"""
for d in range(1007, 1108):
    img_new = img_nondefect.copy()
    x = random.randint(-100, 730)
    y = random.randint(-1400, -750)
    all_pointsx.append(x)
    all_pointsy.append(y)
    img_new.paste(cropped_region, (x, y), cropped_region)
    filename = "C:\\Users\\Johan\\PycharmProjects\\Mask_RCNN_demo\\dataset1\\generated_holes\\bot\\im_" + str(d) + ".jpg"
    img_new.save(filename)

d = 0
for i in range(1007, 1108):
    path = 'C:\\Users\\Johan\\PycharmProjects\\Mask_RCNN_demo\\dataset1\\generated_holes\\bot\\im_' + str(i) + '.jpg'
    size_inbytes = os.path.getsize(path)

    x1 = all_pointsx[d] + poly1[0][0]
    y1 = all_pointsy[d] + poly1[0][1]

    x2 = all_pointsx[d] + poly1[1][0]
    y2 = all_pointsy[d] + poly1[1][1]

    x3 = all_pointsx[d] + poly1[2][0]
    y3 = all_pointsy[d] + poly1[2][1]

    x4 = all_pointsx[d] + poly1[3][0]
    y4 = all_pointsy[d] + poly1[3][1]

    x5 = all_pointsx[d] + poly1[4][0]
    y5 = all_pointsy[d] + poly1[4][1]

    x6 = all_pointsx[d] + poly1[5][0]
    y6 = all_pointsy[d] + poly1[5][1]

    x7 = all_pointsx[d] + poly1[6][0]
    y7 = all_pointsy[d] + poly1[6][1]

    x8 = all_pointsx[d] + poly1[7][0]
    y8 = all_pointsy[d] + poly1[7][1]
    d = d + 1
    #OBS LÄGG TILL MÅSVINGE I BÖRJAN, LÄGG ÄVEN TILL I SLUTET PÅ FILEN OCH TA BORT KOMMA
    string = '"im_' + str(i) + '.jpg' + str(size_inbytes) + '":{"filename":"im_' + str(i) + '.jpg","size":' + str(size_inbytes) + ',"regions":[{"shape_attributes":{"name":"polygon","all_points_x":[' + str(x1) + ',' + str(x2) + ',' + str(x3) + ',' + str(x4) + ',' + str(x5) + ',' + str(x6) + ',' + str(x7) + ',' + str(x8) + '],"all_points_y":[' + str(y1) + ',' + str(y2) + ',' + str(y3) + ',' + str(y4) + ',' + str(y5) + ',' + str(y6) + ',' + str(y7) + ',' + str(y8) + ']},"region_attributes":{"names":"Hole"}}],"file_attributes":{}},'  #ska egentligen va ett komma här på slutet
    with open("artificial_dataset_BR_4.txt", "a") as f:
        # Append some text to the file
        f.write(string)

