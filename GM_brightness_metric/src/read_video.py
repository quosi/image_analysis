import time, os, sys
import cv2
import numpy as np
import concurrent.futures
from gm_metric import GmMetric
import itertools

def image_process(image_info):
    # is processing one image
    status, image = image_info
    print(GmMetric(image, 8).pq_1000())


def read_video(inputpath):
    start_time = time.time()
    path, file = os.path.split(inputpath)
    cap = cv2.VideoCapture(inputpath)
    
    current_frame = 1
    max_frames = 10
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f'Start processing >> {file} << ')
    print(f'Total frames: {total_frames}')

    gm_values = []
    counter = 0
    # read video frame by frame
    while cap.isOpened():
        # create slice of 10 images
        # take 10 images and put them in a (queue) 
        # batch = itertools.islice(cap.read(), 10)
        # print(batch)
        with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
            gm_values = executor.map(image_process, cap.read())



        # print(f'Test mode activ - exit after {max_frames} frames')
        # print(f'Processing time: {round(time.time() - start_time, 2)} sec')
        # print(gm_value_dict)
    cap.release()
    cv2.destroyAllWindows()
    return gm_values

def main():
    test_data = "/Users/pepper/Projekte/PythonProjects/image_analysis_repo/GM_brightness_metric/resources/video/Brosserness_4sec_h264_1920x1080_24fps_2Ch-stereo.mp4"
    read_video(test_data)

if __name__ == "__main__":
    main()