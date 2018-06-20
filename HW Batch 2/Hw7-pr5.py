#Sara D'Alessandro
#Homework #7
#Sunset Filter

import cv2
import numpy as np
from matplotlib import pyplot as plt

def simple_display():
    plt.xticks([]), plt.yticks([]) 
    plt.imshow(image)    
    plt.show()
    input("Hit enter to continue...")

def transform( image ):

    new_image = image.copy()
    num_rows, num_cols, num_chans = new_image.shape
    for row in range(num_rows):
        for col in range(num_cols):
            r, g, b = image[row,col]

            new_image[row,col] = [255, g, 100]

    return new_image

def sunset_filter():

    raw_image = cv2.imread('dog.jpg', cv2.IMREAD_COLOR)
    me = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)
    new_image = transform( me )
    plt.imshow(new_image)
    plt.show()

sunset_filter()