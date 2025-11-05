import cv2
import numpy as np

im = cv2.imread(r"images\image_2025-11-02_03-48-35.png")
im_resized = cv2.resize(im, (300, 300))
cv2.imshow("Original Image", im)
cv2.imshow("Resized Image", im_resized)
cv2.waitKey(0)
