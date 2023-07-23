import os
import cv2
import numpy as np
from varname.helpers import debug

def draw_romb_on_img (img_path, line_color, line_thickness):
    img = cv2.imread(img_path)
    img2draw = img.copy()
    img_height, img_width, img_channels = img2draw.shape
    x_step = int(img_width / 2)
    y_step = int(img_height / 2)
    current_x = 0
    current_y = 0

    for i in range(2):
        previous_y = current_y
        current_y += y_step
        current_x = 0
        if current_y > img_height:
            current_y = img_height
        for j in range(2):
            previous_x = current_x
            current_x += x_step
            if current_x > img_width:
                current_x = img_width
            if i%2 != 0 and j%2==0 or i%2==0 and j%2!=0:
                img2draw = cv2.line(img2draw, pt1=(previous_x, previous_y), pt2=(current_x, current_y), color=line_color, thickness=line_thickness)
            else:
                img2draw = cv2.line(img2draw, pt1=(previous_x, current_y), pt2=(current_x, previous_y), color=line_color, thickness=line_thickness)
    return img2draw

colors_dict = {
    'green':(0, 200, 0),
    'red':(0, 0, 200),
    'blue':(200, 0, 0),
    'black':(0, 0, 0),
    'purple':(255, 0, 139),
    'yellow':(72, 207, 255),
    'light_blue':(255, 191, 0),
    'pink':(203, 192, 255)
    }

chess_jeezus = draw_romb_on_img('jeezus.jpg', colors_dict['pink'], 6)
# print(colors_dict['green'])
cv2.imshow('jeezus', chess_jeezus)
cv2.waitKey(-1)