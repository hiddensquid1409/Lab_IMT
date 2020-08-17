import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 400)
cap.set(4, 400)


while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# Blue color
    high_blue = np.array([126, 255, 255])
    low_blue = np.array([94, 80, 2])  
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

 # Green color
    high_green = np.array([90, 255, 172])
    low_green = np.array([59, 91, 67]) 
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

# Red color
    high_red = np.array([255, 255, 185])
    low_red = np.array([157, 0, 0])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

# Yellow Color
    high_yellow = np.array([187,132,247])
    low_yellow = np.array([29,71,30])
    yellow_mask = cv2.inRange(hsv_frame,low_yellow,high_yellow)
    yellow = cv2.bitwise_and(frame,frame,mask=yellow_mask)

# Orange Color
    high_orange = np.array([255,255,255])
    low_orange = np.array([110,119,148])
    orange_mask = cv2.inRange(hsv_frame,low_orange,high_orange)
    orange = cv2.bitwise_and(frame,frame,mask=orange_mask)

# White Color
    high_white = np.array([144,106,226])
    low_white = np.array([87,0,90])
    white_mask = cv2.inRange(hsv_frame,low_white,high_white)
    white = cv2.bitwise_and(frame,frame,mask=white_mask)



 #Result   
    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)
    cv2.imshow("Yellow", yellow)
    cv2.imshow("Orange", orange)
    cv2.imshow("White", white)


    key = cv2.waitKey(1)
    if key == 27:
        break