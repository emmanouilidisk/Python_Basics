""" Face, Eye and Smile detection in pictures """

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #load cascade file
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') #this is for eye tracking

while True:
    img = cv2.imread('DiCaprio.jpg') #load image file
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert the image to gray
    faces = face_cascade.detectMultiScale(gray, 1.3 ,5) #detect faces
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2) #draw rectangle around faces
        ###Uncomment the following to enable eye tracking:
        #roi_gray=gray[y:y+h, x:x+w]
        #roi_color= img[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
        #   cv2.rectangle(roi_gray, (ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('img',img) #display cascade
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    
cv2.destroyAllWindows()
