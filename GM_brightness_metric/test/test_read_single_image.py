import pytest, logging, os, sys

p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, p)

from src.read_single_image import process_image

def test_process_image():
    test_data = "/Users/pepper/Projekte/PythonProjects/image_analysis_repo/GM_brightness_metric/resources/images/palindrome.png"
    # logging.info('ERROR')
    assert process_image(test_data) is not None, "Failed to process image, check for correct input path!"