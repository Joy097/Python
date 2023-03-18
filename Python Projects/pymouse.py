from turtle import screensize
import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)          #to capture video
hand_detector = mp.solutions.hands.Hands() 
drawing_utils = mp.solutions.drawing_utils
                                   # to detect hand
screen_width,screen_height = pyautogui.size()
index_y=0
while True:                        #run continuously
    _, frame = cap.read()          #read whatever is captured
    frame = cv2.flip(frame,1) # to solve the mirror problem of frame in y axis
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame) #to process
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
                    #calling drawing utils to draw land marks for everypoint of finger
            landmarks = hand.landmark #to get the landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                
                if id == 8:  #only for index finger
                    cv2.circle(img=frame,center=(x,y), radius =10, color =(0,255,0) )
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_width*y
                    pyautogui.moveTo(index_x,index_y)
                

                if id == 4:  #only for thumb finger
                   cv2.circle(img=frame,center=(x,y), radius =10, color =(0,255,0) )
                   thumb_x = screen_width/frame_width*x
                   thumb_y = screen_height/frame_width*y

                   print('outside', abs(index_y - thumb_y))
                   if abs(index_y - thumb_y) <20:
                       pyautogui.click()
                       pyautogui.sleep(1)

    cv2.imshow('Py Mouse', frame)  #show the image
    cv2.waitKey(1)