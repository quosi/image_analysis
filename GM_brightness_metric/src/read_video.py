import time, os, sys
import cv2
import numpy as np
from gm_metric import GmMetric

# for pytest
# from src.gm_metric import GmMetric

def video(inputpath):
    start_time = time.time()
    path, file = os.path.split(inputpath)
    cap = cv2.VideoCapture(inputpath)
    frame_num = 0
    max_frames = 2
    print(f'Start processing >> {file} << ')
    while(frame_num < max_frames):
        # read video frame by frame
        ret, frame = cap.read()
        frame_num += 1
        # add operations to single images
        img = GmMetric(frame, 8)
        print(f'Frame number: {frame_num}')
        img.pq_1000()
        print("Exit processing - test mode: 'activ'")
        print(f'Processing time: {round(time.time() - start_time, 2)} sec')
    return frame

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_data = "/Users/pepper/Projekte/PythonProjects/image_analysis_repo/GM_brightness_metric/resources/video/Brosserness_4sec_h264_1920x1080_24fps_2Ch-stereo.mp4"
    video(test_data)
