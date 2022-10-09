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
from pathlib import Path

# Necessary packages
import numpy
from PIL import Image

# Project modules
from notes import __status__, __email__, __maintainer__, __credits__


############################### GLOBAL CONSTANTS #############################
__author__    = "Martina Terskaya, Darina Ilyukhina and Sergei Abramenkov"
__copyright__ = "Copyright 2022, NSU GeoHack"
__license__   = "MIT"
__version__   = "0.0.2"

# Default velocity model limitations 
V_MIN: float = 0.3 # km/s
V_MAX: float = 2.3 # km/s


############################# CLASSES & FUNCTIONS ############################

class Model2D(numpy.ndarray):
    """A pixelized velocity model.

    Represents quite simple blocky structure of the media in 2D.
    Each block is a square with a constant velocity inside its borders.
    One can set some Xmin/Xmax and Ymin/Ymax as the limits of the model.
    Instead we use h - an arbitrary length of the square block side.
    Therefore:  Xmin = 0, Xmax = h * model.shape[0]
                Ymin = 0, Ymax = h * model.shape[1]
    Adjusting model to fit some arbitrary Xmin/Xmax and Ymin/Ymax is trivial.
    Changing h allows easy scaling of the model to fit different dataset,
    as long as we maintain fixed aspect ratio based on the model shape.

          0   1   2   3   4   5   6   7   8   9
        +---+---+---+---+---+---+---+---+---+---+
        |111|333|222|444|555|444|333|222|444|555|
      0 |111|333|222|444|555|444|333|222|444|555| h
        |111|333|222|444|555|444|333|222|444|555|
        +---+---+---+---+---+---+---+---+---+---+
        |222|333|222|444|555|444|333|222|444|555|
      1 |222|333|222|444|555|444|333|222|444|555| h
        |222|333|222|444|555|444|333|222|444|555|
        +---+---+---+---+---+---+---+---+---+---+
        |444|333|222|444|555|444|333|222|444|555|
      2 |444|333|222|444|555|444|333|222|444|555| h
        |444|333|222|444|555|444|333|222|444|555|
        +---+---+---+---+---+---+---+---+---+---+
          h   h   h   h   h   h   h   h   h   h

    With such representation Model2D class can be an extention of numpy.ndarray.
    We only add couple additional attributes:
        Model2D.name: str - a name for the model
        Model2D.h: float - scaling factor (block size)
    """
    def __new__(cls, input_array, h=1.0, name=None):
        """Normally we would have our model as a standard NumPy array.
        First check if it is two-dimensional (2D) by checking len(array.shape)
        Then if we good, simply casting our Model2D class from it.
        And finally adding model attributes like name and scale.
        """
        obj = numpy.asarray(input_array).view(cls)
        obj.h = h               # Model scale (see class docstring)
        obj.name = name         # Model name (string to identify it by human)
        return obj

    def __array_finalize__(self, obj):
        """Provide a finalization method for class to work properly"""
        if obj is None: return
        self.h = getattr(obj, 'h', None)
        self.name = getattr(obj, 'name', None)
    
    @classmethod
    def from_image(cls, image: Image, vmin=V_MIN, vmax=V_MAX):
        """Convert image to grayscale and creating model from it.
        An alternative constructor of class instance.
        More about @classmethod decorator:
            https://www.youtube.com/watch?v=rq8cL2XMM5M
        """
        #print(type(image))
        gray_scale = image.convert(mode='L')
        velmod = numpy.asarray(gray_scale) / 255 * (vmax - vmin) + vmin
        print(type(velmod))
        print(velmod.shape)
        return Model2D(velmod)
    

def read_image_as_model(path: Path):
    try:
        image = Image.open(path)
    except FileNotFoundError:
        pass
    #image.show()
    return Model2D.from_image(image)

#def write_model_as_image(model: Model2D, path: Path, colorscale='gray'):
    

############################### SCRIPT BEHAIVIOR #############################
if __name__ == '__main__':
    for i, arg in enumerate(sys.argv):
        print(f'Command line argument {i}: {arg}')
    if len(sys.argv) == 2:
        print(f'Reading {sys.argv[1]} picture as a velocity model')
        model = read_image_as_model(Path(sys.argv[1]))
        print(type(model))
        print(model.name)
        print(model.h)
        print(model)
    print(f'Exiting script {__file__} without errors.')
    exit(0)
