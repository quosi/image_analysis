import math
import statistics
import cv2
from cv2 import VideoCapture, VideoWriter
import numpy as np
from numpy.core.defchararray import join

class GmMetric:
    """Calculation of average HDR brightness by using GM (geometric mean) metric
    for evaluation of average pixel luminance (APL) level in HDR images.
    Metric proposed by Ploumis, Boitard, Jacquemin, Damberg, Ballestad, Nasiopoulos
    in 'Quantitative Evaluation and Attribute of Overall Brightness in High Dynamic Range World'
    presented at SMPTE 2018 conference, LA.
    INPUT: single RGB image as numpy array
    OUTPUT: integer value of GM pixel luminance value"""

    def __init__(self, img_in, bit_depth):
        self.img = img_in
        # bit_depth of image_in (single frame of img_in)
        self.n = bit_depth
        # number of pixel (i.e. HD image: 1920x1080)
        self.num_pixel = self.img.shape[0]*self.img.shape[1]

    def load(self):
        """Loading single image and preparing data for processing,
        unpacking 3D-array (single image) into list of pixel values
        INPUT: single RGB image as numpy array
        OUTPUT: list of pixel values"""
        text = "Collecting pixel values ..."
        img_RGB = self.img
        img_gray = cv2.cvtColor(img_RGB, cv2.COLOR_BGR2GRAY)
  
        print(text)
        img_R, img_G, img_B = [img_RGB[:,:,channel].astype(float) for channel in range(0, 3, 1)]
        # slice input of each channel into single rows of pixels to calculate the variance & gm_log
        pixel_list_R = img_R.ravel()
        pixel_list_G = img_G.ravel()
        pixel_list_B = img_B.ravel()
        pixel_list = pixel_list_R
        pixel_list = np.append(pixel_list, pixel_list_G)
        pixel_list = np.append(pixel_list, pixel_list_B)
        pixel_list_gray = img_gray.ravel()
        return pixel_list

    def gm_log(self, pixel_list):
        """Calculation of geometric mean value for list of pixel values (1D-array or list)"""
        #sum_of_log = math.fsum(math.log(x) for x in pixel_list)
        sum_of_log = 0.0
        num_black_pixel = 0
        for x in pixel_list:
            if x == 0:
                num_black_pixel +=1
                # step over pixel with zero-value and continues for-loop
                continue
            sum_of_log = sum_of_log + math.log(x)
        print(f'Number of black pixel: {num_black_pixel}')
        return math.exp(sum_of_log / len(pixel_list))

    def metric(self):
        """Calculating geometric mean pixel luminance value for one image
        OUTPUT: integer value"""
        img = self.load()
        gm_log_value = self.gm_log(img)
        value = math.sqrt(0.65 * (gm_log_value ** 2) + 0.35 * statistics.variance(img)) / 2 ** (self.n - 1)
        # note: deleted math.exp metric(), used in gm_log()
        print(f'GM pixel luminance value: {round(value, 2)}')
        return value

    def pq_1000(self):
        """Calculating normalized metric by PQ code value associated 
        with the peak luminance of mastering display (1.000nits)
        (page 8 of above cited paper)"""
        pq_norm_value = (self.metric()/1000)*100
        print(f'PQ normalized GM-PL value: {round(pq_norm_value, 2)}') 
        return pq_norm_value
