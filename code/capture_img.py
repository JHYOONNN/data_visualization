# capture video every time_quantum seconds

import cv2
import math

videoFile = "./video/emotion_test.mp4"

cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
time_quantum = 1 # standard second to capture

def capture_video():
    x=0
    while(cap.isOpened()):
        frameId = cap.get(1) #current frame number
        ret, frame = cap.read()
        if (ret != True):
            break
        if (frameId % math.floor(frameRate*time_quantum) == 0):
            print("captured frame : ", frameId)
            filename = './capture/' +  str(int(x)) + ".jpg"
            x+=1
            cv2.imwrite(filename, frame)
    print(x)
    return x

    cap.release()
print ("Done!")