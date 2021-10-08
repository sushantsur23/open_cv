import cv2
import numpy as np

path = 'resources/tony.jpg'
img = cv2.imread(path)

imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("Original",img)
cv2.imshow("new image",imgHSV)
cv2.waitKey(0)
