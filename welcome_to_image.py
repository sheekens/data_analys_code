#python3 welcome_to_image.py

import os
import cv2
import numpy as np

img_path = os.path.abspath('jeezus.jpg')
# img_path = os.path.abspath('uz.jpg')
print(img_path)

img = cv2.imread(img_path)
print(img.shape)
img_height, img_width, img_channels = img.shape
# print(img_height, img_width)
img_top = img[:100,:,:]
out_path = 'top_jeezus.jpg'
cv2.imwrite(out_path, img_top)
# print('written to',os.path.abspath(out_path))
img_left = img[:,200:400,:]
out_path = 'left_jeezus.jpg'
cv2.imwrite(out_path, img_left)
# print('written to',os.path.abspath(out_path))
img_center = img[350:450,250:450,:]
out_path = 'center_jeezus.jpg'
cv2.imwrite(out_path, img_center)
# print('written to',os.path.abspath(out_path))

# pupok = img_center.copy()
# pupok = cv2.resize(pupok, dsize=None, fx=4.0, fy=4.0)
# print(pupok.shape)
# pupok[:,:,0] = 255 #blue kanal = 0
# # pupok[:,:,2] = 255 #red kanal = 0
# print(pupok)
# cv2.imshow('jeezus', pupok)
# cv2.waitKey(-1)

w_divider = 11
h_divider = w_divider
x_step = int(img_width / w_divider)
y_step = int(img_height / h_divider)
current_x = 0
current_y = 0

for i in range(w_divider):
    previous_y = current_y
    current_y += y_step
    current_x = 0
    for j in range(h_divider):
        previous_x = current_x
        current_x += x_step
        preprevious_x = previous_x - x_step
        if i%2 == 0 and j%2 == 0:
            print('2 for x:', previous_x, current_x, 'y:', previous_y, current_y)
            crop = img[
                previous_y:current_y,
                previous_x:current_x,
                :
            ]
            crop *= 0
        elif i%2 != 0 and j%2 == 0:
            print('3 for x:', previous_x, current_x, 'y:', previous_y, current_y)
            crop = img[
                previous_y:current_y,
                preprevious_x:previous_x,
                :
            ]
            crop *= 0

cv2.imshow('jeezus', img)
cv2.waitKey(-1)
