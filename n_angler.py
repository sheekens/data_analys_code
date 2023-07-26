import os
import cv2
import numpy as np
from varname.helpers import debug

img_path = os.path.abspath('uz.jpg')

img = cv2.imread(img_path)

def axis_for_n_angler(img, center_xy, radius, axis_line_color, axis_line_thickness):
    img2draw = cv2.imread(img)
    axis_x_pt1 = (center_xy[0]-radius-10,
        center_xy[1])
    axis_x_pt2 = (center_xy[0]+radius+10,
        center_xy[1])
    axis_y_pt1 = (center_xy[0],
        center_xy[1]-radius-10)
    axis_y_pt2 = (center_xy[0],
        center_xy[1]+radius+10)

    img2draw = cv2.line(img2draw, axis_x_pt1, axis_x_pt2, axis_line_color, axis_line_thickness)
    img2draw = cv2.line(img2draw, axis_y_pt1, axis_y_pt2, axis_line_color, axis_line_thickness)
    return img2draw

def n_angler(img, n, radius, center_xy, line_color, line_thickness, axis_flag, axis_line_color, axis_line_thickness):
    img2draw = cv2.imread(img)
    if axis_flag == True:
        img2draw = axis_for_n_angler(
            img, center_xy, radius, axis_line_color, axis_line_thickness
            )
    angle_step = 2*np.pi/n
    
    current_x = int(radius*np.cos(angle_step) + center_xy[0])
    current_y = int(radius*np.sin(angle_step) + center_xy[1])

    for step in range(n+1):
        angle = step*angle_step
        previous_x = current_x
        previous_y = current_y

        current_x = int(radius*np.cos(angle) + center_xy[0])
        current_y = int(radius*np.sin(angle) + center_xy[1])
        img2draw = cv2.line(
            img=img2draw,
            pt1=(previous_x, previous_y),
            pt2=(current_x, current_y),
            color=line_color,
            thickness=line_thickness
        )
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

img2draw = n_angler(
    img=img_path,
    n=10,
    radius=100,
    center_xy=(230, 170),
    line_color=colors_dict['pink'],
    line_thickness=3,
    axis_flag=True,
    axis_line_color=colors_dict['green'],
    axis_line_thickness=2
) 

cv2.imshow('jeezus', img2draw)
cv2.waitKey(-1)