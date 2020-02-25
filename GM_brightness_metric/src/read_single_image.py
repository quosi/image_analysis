import time, os
import cv2
import numpy as np

from gm_metric import GmMetric

def process_image(inputpath):
    # get system time to calculate processing
    start_time = time.time()
    # get input file & start processing
    path, file = os.path.split(inputpath)
    print(f'Start processing >> {file} << ')
    img = cv2.imread(inputpath)
    gm_metric_object = GmMetric(img, 8)
    result = gm_metric_object.metric() #.pq_1000()
    # stop & print processing time
    print(f'Processing time: {round(time.time() - start_time, 2)} sec')

    return result

if __name__ == "__main__":
    test_data = "/Users/pepper/Projekte/PythonProjects/image_analysis_repo/GM_brightness_metric/resources/images/palindrome.png"
    process_image(test_data)

