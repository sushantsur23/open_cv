#Murtaza's Workshop - Robotics and AI
import cv2
import numpy as np

#import and read an image
img = cv2.imread('resources/photo1.jpg')
cv2.imshow("Output",img)
#add waiting time 
cv2.waitKey(0)

#video capture object 
cap = cv2.VideoCapture('resources/video.mp4')

#here while loop is used to capture all the frames of the video
#press Q while the video runs to stop it in case its a long one.
# the if condition is making the video to wait for the time tie video finished runnung completely
while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break

#creating a webcam object and defining parameters for the same
# in case of additional webcams update VideoCapture(1 or more)
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
#setting brightness
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break


#converting photo to grey scale
img = cv2.imread('resources/photo2.jpg')

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)

#Making an blurr image
img = cv2.imread('resources/photo3.jpg')

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,ksize=(19,19),sigmaX =0)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)

cv2.waitKey(0)


#Edge detector and dialation
img = cv2.imread('resources/photo3.jpg')

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,ksize=(19,19),sigmaX =0)
imgCanny = cv2.Canny(img,100,100)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.waitKey(0)

#Edge detector and dialation
#Dilation adds pixels to the boundaries of objects in an image

img = cv2.imread('resources/photo3.jpg')
kernel = np.ones((5,5),np.uint8)

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,ksize=(19,19),sigmaX =0)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Canny Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)

#work with images and attributes of the same

img = cv2.imread('resources/thor.jpg')
print(img.shape)
imgResize=cv2.resize(img,(930,810))
#image cropping
imgCropped = img[0:200,200:500]

cv2.imshow("Image",img)
cv2.imshow("Resized Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)
cv2.waitKey(0)

#Shapes and texts
#need to add 3 channels to make it colored image
img = np.zeros((512,512,3),np.uint8)
# : means to color the whole image or else we need to add channels as per below
# img[200:300,100:300] = 255,0,0 partial coloring
#coloring whole box
#img[:] = 255,0,0

cv2.line(img,(0,0),(300,300),(0,250,0),3)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,250,0),3)
cv2.rectangle(ing,(0,0),(250,300),(0,0,255),2)
# to fill your rectangle
cv2.rectangle(ing,(0,0),(250,300),(0,0,255),cv2.FILLED)

cv2.imshow("Image",img)
cv1.waitKey(0)