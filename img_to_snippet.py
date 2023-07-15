#python3 welcome_to_image.py

import os
import cv2
import numpy as np

img_path = os.path.abspath('jeezus.jpg')

img = cv2.imread(img_path)
img_height, img_width, img_channels = img.shape

def img_to_snippet (img_path, w_divider, h_divider):
    img = cv2.imread(img_path)
    img_name, extension = os.path.splitext(img_path)
    print(img_name)
    x_step = int(img_width / w_divider)
    y_step = int(img_height / h_divider)
    current_x = 0
    current_y = 0

    for i in range(h_divider + 1):
        previous_y = current_y
        current_y += y_step
        current_x = 0
        if current_y > img_height:
            current_y = img_height
        for j in range(w_divider + 1):
            previous_x = current_x
            current_x += x_step
            if current_x > img_width:
                current_x = img_width
            crop = img[
                previous_y:current_y,
                previous_x:current_x,
                :
            ]
            crop_x1 = previous_x
            crop_y1 = previous_y
            crop_x2 = current_x
            crop_y2 = current_y
            crop_name = '{}.x1_{}.y1_{}.x2_{}.y2_{}.{}'.format(img_name, crop_x1, crop_y1, crop_x2, crop_y2, extension)
            out_path = '{}\{}'.format(img_name, crop_name)
            cv2.imwrite(out_path, crop)
    return img

chess_jeezus = img_to_snippet('jeezus.jpg', 7, 22)
cv2.imshow('jeezus', chess_jeezus)
cv2.waitKey(-1)
