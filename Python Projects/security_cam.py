import cv2
import winsound
import os

cam = cv2.VideoCapture(0)

a=0

while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1,frame2) # difference between frames
    grey = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(grey,(5,5),0)
    _,thresh = cv2.threshold(blur,20, 255,cv2.THRESH_BINARY) #read of noises of unwanted things
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   # cv2.drawContours(frame1, contours, -1, (255,0,0),2)
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (255,0,0),2 )
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
        # winsound.Beep(500,200)
        a=a+1
        cv2.imwrite('C:/Users/User/Desktop/baebo/sec_imgs/a'+str(a)+'.png',frame1) #save the photo detected in the directory
    if cv2.waitKey(10) == ord('q'):
        break # q will quit from the camera
    cv2.imshow('Security Cam', frame1) #show difference