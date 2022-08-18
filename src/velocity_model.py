#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TomoHack/src/velocity_model.py

"""We import image, change the color to the white-black spectrum
and make the array from the pixels.
"""

import sys      # Python standard library (interpreter related functions)

from PIL import Image
from numpy import asarray


__author__ = ["Martina Terskaya", "Darina Ilyukhina"]
__copyright__ = ["Darina Ilyukhina", "Martina Terskaya"]
__credits__ = ["Sergei Abramenkov","Darina Ilyukhina", "Martina Terskaya", 
                "Kristina Potapova", "Vasiliy Potapov"]
__license__ = "MIT"
__version__ = "0.0.1"


V_MIN = 0.3 # km/s
V_MAX = 2.3 # km/s

def read_picture(path):
    image = Image.open(path) 
    print(image.mode)
    gray_scale = image.convert(mode='L')
    #gray_scale.show() 
    print(gray_scale.mode)
    
    velmod = asarray(gray_scale)
    print(type(velmod))
    velmod = velmod / 255 * (V_MAX - V_MIN) + V_MIN     
    print(velmod)
    return(velmod)
    


if __name__ == '__main__':
    print(f'Arguments count: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument {i}: {arg}')
    if len(sys.argv) == 2:
        read_picture(sys.argv[1])

