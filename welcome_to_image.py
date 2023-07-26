import os
import cv2
import numpy as np
from varname.helpers import debug

img_path = os.path.abspath('jeezus.jpg')

img = cv2.imread(img_path)
img_height, img_width, img_channels = img.shape
img_top = img[:100,:,:]
out_path = 'top_jeezus.jpg'
cv2.imwrite(out_path, img_top)
img_left = img[:,200:400,:]
out_path = 'left_jeezus.jpg'
cv2.imwrite(out_path, img_left)
img_center = img[350:450,250:450,:]
out_path = 'center_jeezus.jpg'
cv2.imwrite(out_path, img_center)

def image_into_chess (img_path, w_divider, h_divider):
    img = cv2.imread(img_path)
    img_height, img_width, img_channels = img.shape
    x_step = int(img_width / w_divider)
    y_step = int(img_height / h_divider)
    current_x = 0
    current_y = 0

    for i in range(h_divider+1):
        previous_y = current_y
        current_y += y_step
        current_x = 0
        if current_y > img_height:
            current_y = img_height
        for j in range(w_divider+1):
            previous_x = current_x
            current_x += x_step
            if current_x > img_width:
                current_x = img_width
            preprevious_x = previous_x - x_step
            if i%2 != 0 and j%2 != 0:
                crop = img[
                    previous_y:current_y,
                    previous_x:current_x,
                    :
                ]
                crop *= 0
            elif i%2 == 0 and j%2 != 0:
                crop = img[
                    previous_y:current_y,
                    preprevious_x:previous_x,
                    :
                ]
                crop *= 0
    return img

chess_jeezus = image_into_chess('uz.jpg', 9, 12)
cv2.imshow('jeezus', chess_jeezus)
cv2.waitKey(-1)
