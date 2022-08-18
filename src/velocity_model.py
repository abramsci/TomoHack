#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TomoHack/src/velocity_model.py

"""Functions related to the parametrization of a velocity model.

Can be used as a script with command line arguments.
Module is primarily based on NumPy package for linear algebra manipulations.
Python Image Library (PIL) is used for picture reading and drawing.
"""
################################### IMPORTS ##################################

# Python standard library imports
import sys

# Necessary packages
from PIL import Image
from numpy import asarray

# Project modules
from notes import __status__, __email__, __maintainer__, __credits__


############################### GLOBAL CONSTANTS #############################
__author__    = "Martina Terskaya, Darina Ilyukhina and Sergei Abramenkov"
__copyright__ = "Copyright 2022, NSU GeoHack"
__license__   = "MIT"
__version__   = "0.0.2"

# Velocity limitations for a model
V_MIN = 0.3 # km/s
V_MAX = 2.3 # km/s


############################# CLASSES & FUNCTIONS ############################

"""Read image, change colorspace to grayscale and make NumPy array from it.
"""
def read_picture(path):
    image = Image.open(path) 
    gray_scale = image.convert(mode='L')
    image.show()
    gray_scale.show()
    print(image.mode)
    print(gray_scale.mode)
    
    velmod = asarray(gray_scale)
    print(type(velmod))
    velmod = velmod / 255 * (V_MAX - V_MIN) + V_MIN     
    print(velmod)
    return(velmod)
    

############################### SCRIPT BEHAIVIOR #############################
if __name__ == '__main__':
    for i, arg in enumerate(sys.argv):
        print(f'Command line argument {i}: {arg}')
    if len(sys.argv) == 2:
        print(f'Reading {sys.argv[1]} picture as a velocity model')
        read_picture(sys.argv[1])
    print(f'Exiting script {__file__} without errors.')
    exit(0)
