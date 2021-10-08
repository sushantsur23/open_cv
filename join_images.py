import cv2
import numpy as np
#images needs to be of same no of channels as we are dealing with matrix.
img = cv2.imread('resources/tony.jpg')

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)
cv2.waitKey(0)
#disadvantage is the the picture might go out of frame