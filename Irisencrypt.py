'''imports'''

#import image processing module 
import cv2
#import math functions 
import numpy as np
#import polar coordinate conversion module 
from skimage.transform import warp_polar
#import function that converts our iris to a unique code 
import hashlib

'''
function to convert the image to grayscale to make it more efficient 
then use median blur to reduce the noise 
''' 
def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.medianBlur(img, 5)
    return img
