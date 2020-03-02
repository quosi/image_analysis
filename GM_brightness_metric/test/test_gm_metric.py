import pytest, logging, cv2, os, sys
import numpy as np

p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, p)

from src.gm_metric import GmMetric

def test_load_RGB():
    test_data = "/Users/pepper/Projekte/PythonProjects/image_analysis_repo/GM_brightness_metric/resources/images/ecosia.jpg"
    image = cv2.imread(test_data, cv2.IMREAD_UNCHANGED)
    height = image.shape[0]
    width = image.shape[1]
    # channels = image.shape[2] 
    gm_metric_object = GmMetric(image, 8)
    result = gm_metric_object.load() #.pq_1000()
    print(height * width)
    assert np.zeros(height * width).shape == result.shape, "1. Check correct input path, 2. Check number of colour channels."

def test_pq_1000():
    test_data = "/Users/pepper/Projekte/PythonProjects/image_analysis_repo/GM_brightness_metric/resources/images/ecosia.jpg"
    image = cv2.imread(test_data, cv2.IMREAD_UNCHANGED)
    result = GmMetric(image, 8)
    assert type(result.pq_1000()) == type(10.)

def test_metric():
    test_data = "/Users/pepper/Projekte/PythonProjects/image_analysis_repo/GM_brightness_metric/resources/images/ecosia.jpg"
    image = cv2.imread(test_data, cv2.IMREAD_UNCHANGED)
    result = GmMetric(image, 8)
    assert type(result.metric()) == type(10.)