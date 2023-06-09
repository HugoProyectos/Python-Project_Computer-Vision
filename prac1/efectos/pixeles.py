import cv2 # Import python-supported OpenCV functions
import numpy as np # Import numpy and call it np
from matplotlib import pyplot as plt # Import pyplot and call it plt

def apply(image, pixel_size):
    
    # Pixel size
    w, h  = (int(pixel_size), int(pixel_size))
    height,width = image.shape[:2]

    aux_img = cv2.resize(image,(w,h))

    # interpolation=cv2.INTER_NEAREST nearest-neighbor interpolation
    new_img = cv2.resize(aux_img, (width,height), interpolation=cv2.INTER_NEAREST)
    
    return new_img