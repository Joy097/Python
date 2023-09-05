import cv2
import cvzone

bg = cv2.imread('jkr.png')
overlay = cv2.imread('sunglass.png',cv2.IMREAD_UNCHANGED)
final_image = cvzone.overlayPNG(bg,overlay,[100,100])
cv2.imshow('Result Image',final_image)
cv2.waitKey(0)
