import cv2
import numpy as np
img=cv2.imread("ball_image.jpeg",1)
# function get you coordinate of mouse
"""def click_event(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        text=str(x)+" ,"+str(y)
        cv2.putText(img,text,(x,y),font,1,(255,0,0),3)
        cv2.imshow("frame",img)"""

ball=img[259:410, 465:634] #y1:y2   x1:x2
img[161:312 , 68:237]=ball #copy it in other coordinate
cv2.imshow("frame",img)
#cv2.setMouseCallback("frame",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
