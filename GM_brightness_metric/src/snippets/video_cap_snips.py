import time, os, sys
import cv2
import numpy as np

p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, p)
from gm_metric import GmMetric

def video(inputpath):
    start_time = time.time()
    path, file = os.path.split(inputpath)
    cap = cv2.VideoCapture(inputpath)
    max_frames = 2
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    counter = 0
    current_frame = iter(list(range(1, max_frames+1, 1)))

    while(counter < max_frames):
        # read video frame by frame
        gm_value_dict = map(lambda frame: {next(current_frame): frame[1][1][1]}, cap.read()[1])
        print(f'RESULT: {gm_value_dict}')
        print(f'Processing time: {round(time.time() - start_time, 2)} sec')
        counter +=1

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_data = "/Users/pepper/Projekte/PythonProjects/GM_brightness_metric/video/Brosserness_4sec_h264_1920x1080_24fps_2Ch-stereo.mp4"
    video(test_data)
