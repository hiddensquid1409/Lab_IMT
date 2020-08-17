#Import necessary libraries for the webcam to work 
import numpy as np
import cv2
import time


# Initialization variables for the webcam Object and the list
# of all the colors available in the Rubik's Cube
cap = cv2.VideoCapture(0)


#Throw an error if webcam is not available
if not cap.isOpened(): 
    raise IOError("Can't Open webcam")

# Initial Values for the HSV Parameters (Lower and Upper)

# (TODO)
# Change this to array format

uh = 255
us = 255
uv = 255
lh = 0 
ls = 0
lv = 0 
upper_hsv = np.array([uh,us,uv])
lower_hsv = np.array([lh,ls,lv])


window_name = "HSV Calibrator"

cv2.namedWindow(window_name)
cv2.resizeWindow(window_name,600,600)

def nothing(x): 
    print("Trackbar Value : " + str(x))
    pass

# create trackbars for Upper HSV 
cv2.createTrackbar('UpperH', window_name, 0, 255, nothing)
cv2.setTrackbarPos('UpperH', window_name,uh)

cv2.createTrackbar('UpperS', window_name,0,255,nothing)
cv2.setTrackbarPos('UpperS', window_name, us)

cv2.createTrackbar('UpperV', window_name,0,255, nothing)
cv2.setTrackbarPos('UpperV', window_name,uv)

# create trackbars for Lower HSV    
cv2.createTrackbar('LowerH', window_name, 0, 255, nothing)
cv2.setTrackbarPos('LowerH', window_name,lh)

cv2.createTrackbar('LowerS', window_name,0,255,nothing)
cv2.setTrackbarPos('LowerS', window_name, ls)

cv2.createTrackbar('LowerV', window_name,0,255, nothing)
cv2.setTrackbarPos('LowerV', window_name,lv)

#Styling
font = cv2.FONT_HERSHEY_SIMPLEX


# Endless loop that will be in charge of adjusting the HSV parameters to the desired levels


while(True):
    # The Calibration Process 
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    cv2.putText(mask,'Lower HSV: [' + str(lh) +',' + str(ls) + ',' + str(lv) + ']', (10,30), font, 0.5, (200,255,155), 1, cv2.LINE_AA)
    cv2.putText(mask,'Upper HSV: [' + str(uh) +',' + str(us) + ',' + str(uv) + ']', (10,60), font, 0.5, (200,255,155), 1, cv2.LINE_AA)

    cv2.imshow(window_name,mask)
    cv2.imshow("webcam", frame)


# IF esc is pressed: break the loop 

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    # get current positions of Upper HSV trackbars
    uh = cv2.getTrackbarPos('UpperH',window_name)
    us = cv2.getTrackbarPos('UpperS',window_name)
    uv = cv2.getTrackbarPos('UpperV',window_name)
    # get current positions of Lower HSV trackbars
    lh = cv2.getTrackbarPos('LowerH',window_name)
    ls = cv2.getTrackbarPos('LowerS',window_name)
    lv = cv2.getTrackbarPos('LowerV',window_name)
    upper_hsv = np.array([uh,us,uv])
    lower_hsv = np.array([lh,ls,lv])

    time.sleep(.1)
#End of cycle 


cap.release()
cv2.destroyAllWindows()

#EOF 