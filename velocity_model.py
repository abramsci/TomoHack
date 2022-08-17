#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TomoHack/src/velocity_model.py

"""

"""

import sys      # Python standard library (interpreter related functions)

__author__ = ["Sergei Abramenkov", "Darina Ilyukhina", "Martina Terskaya"]
__copyright__ = "Darina Ilyukhina", "Martina Terskaya"
__credits__ = ["Sergei Abramenkov","Darina Ilyukhina", "Martina Terskaya", 
                "Kristina Potapova", "Vasiliy Potapov"]
__license__ = "MIT"
__version__ = "0.0.1"



"""We import jpg. image, change the color to the white-black spectrum
and make the array from the pixels.
"""

import random
from PIL import Image, ImageDraw   
import numpy as np    
from numpy import asarray

def read_picture (path):
    image = Image.open(r"C:\Users\Мартина\Documents\GeoHack\earth.jpg")
    draw = ImageDraw.Draw(image) 
#image.show()
#width = image.size[0] #Определяем ширину. 
#height = image.size[1] #Определяем высоту. 	
#pix = image.load() #Выгружаем значения пикселей.

    if (mode == 0):
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a + b + c) // 3
                draw.point((i, j), (S, S, S))
#image.show()

    numpydata = asarray(image)
    #print(type(numpydata))
    #print(numpydata.shape)
    return(numpydata)

if __name__ == '__main__':
    print(f'Arguments count: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument {i}: {arg}')
    if len(sys.argv) == 2:
        read_picture(sys.argv[1])

