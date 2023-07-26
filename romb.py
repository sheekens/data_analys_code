import os
import cv2
import numpy as np
from varname.helpers import debug

def draw_romb (img_path, top_left_xy, bot_right_xy, line_color, line_thickness):
    img = cv2.imread(img_path)
    img2draw = img.copy()
    debug(img2draw.shape)
    bbox_height = abs(bot_right_xy[1] - top_left_xy[1])
    bbox_width = abs(bot_right_xy[0] - top_left_xy[0])
    
    x_step = int(bbox_width / 2)
    y_step = int(bbox_height / 2)
    current_x = top_left_xy[0]
    current_y = top_left_xy[1]

    img2draw = cv2.rectangle(img2draw, top_left_xy, bot_right_xy, colors_dict['blue'], line_thickness)
    for i in range(2):
        previous_y = current_y
        current_y += y_step
        current_x = top_left_xy[0]
        for j in range(2):
            previous_x = current_x
            current_x += x_step
            if i%2 != 0 and j%2==0 or i%2==0 and j%2!=0:
                img2draw = cv2.line(img2draw, pt1=(previous_x, previous_y), pt2=(current_x, current_y), color=line_color, thickness=line_thickness)
                debug(previous_x, previous_y, current_x, current_y)
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

pt1_top_left_xy = (30, 20)
pt2_bot_right_xy = (480, 40)
chess_jeezus = draw_romb(
    img_path='uz.jpg',
    top_left_xy=pt1_top_left_xy,
    bot_right_xy=pt2_bot_right_xy,
    line_color=colors_dict['pink'],
    line_thickness=1)
cv2.imshow('jeezus', chess_jeezus)
cv2.waitKey(-1)