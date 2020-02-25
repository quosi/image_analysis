import time, os
import cv2
import numpy as np

from gm_metric import GmMetric

def read_image(inputpath):
    # get system time for timing process
    start_time = time.time()
    # get input file & start processing
    path, file = os.path.split(inputpath)
    print(f'Start processing >> {file} << ')
    img = cv2.imread(inputpath)
    result = GmMetric(img, 8).metric() #.pq_1000()
    # stopping processing time
    print(f'Processing time: {round(time.time() - start_time, 2)} sec')

if __name__ == "__main__":
    test_data = "/Users/pepper/Projekte/PythonProjects/image_analysis_repo/GM_brightness_metric/resources/images/wall.jpg"
    read_image(test_data)
