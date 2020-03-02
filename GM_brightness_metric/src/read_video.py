import time, os, sys
import cv2
import numpy as np
import concurrent.futures
from gm_metric import GmMetric

def read_video(inputpath):
    start_time = time.time()
    path, file = os.path.split(inputpath)
    cap = cv2.VideoCapture(inputpath)
    current_frame = 1
    max_frames = 10
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f'Start processing >> {file} << ')
    print(f'Total frames: {total_frames}')
    gm_value_dict = {}
    counter = 0
    # read video frame by frame
    with concurrent.futures.ProcessPoolExecutor() as executor:
        while (counter < max_frames):
            current_frame = iter(list(range(1, total_frames+1, 1)))
            gm_value_dict = executor.map(lambda frame: {next(current_frame): GmMetric(frame, 8).pq_1000()}, cap.read()[1])
            counter += 1

        print(f'Test mode activ - exit after {max_frames} frames')
        print(f'Processing time: {round(time.time() - start_time, 2)} sec')
        print(gm_value_dict)
        cap.release()
        cv2.destroyAllWindows()
    return gm_value_dict

if __name__ == "__main__":
    test_data = "/Users/pepper/Projekte/PythonProjects/image_analysis_repo/GM_brightness_metric/resources/video/Brosserness_4sec_h264_1920x1080_24fps_2Ch-stereo.mp4"
    read_video(test_data)
