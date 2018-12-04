# capture video every time_quantum seconds

import cv2
import math

videoFile = "./video/emotion_test.mp4"


class capture_video:
    def __init__(self, video_file_route):
        self.video_route = video_file_route
        self.cap = cv2.VideoCapture(video_file_route)
        self.frame_rate = self.cap.get(5) # get frame rate
        self.time_quantum = 1 # standard second to capture
        
    def capture_video_def(self):
        count_temp = 0
        while(self.cap.isOpened()):
            frameId = self.cap.get(1) #current frame number
            ret, frame = self.cap.read()
            if (ret != True):
                break
            if (frameId % math.floor(self.frame_rate * self.time_quantum) == 0):
                file_path = './capture/'
                file_name = file_path +  str(int(count_temp)) + ".jpg"
                count_temp += 1
                cv2.imwrite(file_name, frame)
        self.cap.release()
        
        return count_temp, file_path
        

class main:
    def __init__(self, video_file):
        self._capture_video = capture_video(video_file).capture_video_def()
        print("capturing complete : ", self._capture_video[0], " of jpg file created at : ", self._capture_video[1])

    def return_value(self):
        return self._capture_video
if __name__ == "__main__":
    main()