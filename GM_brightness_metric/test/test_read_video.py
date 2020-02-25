import pytest, logging
from read_video import read_video

def test_read_video():
    test_data = "/Users/pepper/Projekte/PythonProjects/GM_brightness_metric/resources/video/Brosserness_4sec_h264_1920x1080_24fps_2Ch-stereo.mp4"
    #logging.info('ERROR')
    i = 0
    for frame in read_video(test_data):
        logging.info("Output in loop")
        assert frame is not None, "fail"
        i+=1
    assert i>0
