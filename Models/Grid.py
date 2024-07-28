import cv2 #Use this to get dimensions
import numpy
lastHope = cv2.VideoCapture("testVideos/cartop.mp4") 
widthOfFrame = int(lastHope.get(cv2.CAP_PROP_FRAME_WIDTH))
heightOfFrame = int(lastHope.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(widthOfFrame,heightOfFrame)  
