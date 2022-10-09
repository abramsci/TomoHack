#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TomoHack/src/ray_tracing.py

"""...
"""

################################### IMPORTS ##################################

# Python standard library imports
import sys
import math

# Necessary packages
import numpy

# Project modules (in the same folder/repo)
from velocity_model import Model2D
from notes import __status__, __email__, __maintainer__, __credits__

############################### GLOBAL CONSTANTS #############################
__author__    = "Martina Terskaya, Darina Ilyukhina and Sergei Abramenkov"
__copyright__ = "Copyright 2022, NSU GeoHack"
__license__   = "MIT"
__version__   = "0.0.2"


H = 1.0
TEST_MODEL = Model2D(numpy.array([[1, 2, 3, 4, 5], 
                                [6, 7, 8, 9, 10],
                                [11, 12, 13, 14, 15]]),
                                h=H, name='testmodel')
"""Test velocity model:

          0   1   2   3   4 
        +---+---+---+---+---+
        |111|222|333|444|555|
      0 |111|2S2|333|444|555| h
        |111|222|333|444|555|
        +---+---+---+---+---+
        |666|777|888|999|AAA|
      1 |666|777|888|999|AAA| h
        |666|777|888|999|AAA|
        +---+---+---+---+---+
        |BBB|CCC|DDD|EEE|FFF|
      2 |BRB|CCC|DDD|EEE|FFF| h
        |BBB|CCC|DDD|EEE|FFF|
        +---+---+---+---+---+
          h   h   h   h   h
"""

S = (0, 1)
R = (2, 0)


############################# CLASSES & FUNCTIONS ############################

class Ray2D():
    
    def __init__(self, source_pos: int, receiver_pos: int):
        self.s = source_pos
        self.r = receiver_pos
        self.t = None 
        
    def trace(self, model: Model2D):
        """Trace itself in some velocity model"""
        # Obtaining straight line equation
        a = (self.s[1] - self.r[1]) / (self.s[0] - self.r[0])
        b = model.h * (self.s[1] + 0.5 - a * (self.s[0] + 0.5))
        print(f"y = {a}x + {b}")
        print(f"x = (y - {b}) / {a}")

        # Looking for points on block edges
        points = []
        i_start = min(self.s[0], self.r[0]) + 1
        i_end = max(self.s[0], self.r[0]) + 1
        for i in range(i_start, i_end):
            points.append((i* model.h, a * i * model.h + b))
        print(points)
        j_start = min(self.s[1], self.r[1]) + 1
        j_end = max(self.s[1], self.r[1]) + 1
        for j in range(j_start, j_end):
            points.append(((j * model.h - b) / a, j * model.h))

        points.append(((self.s[0] + 0.5) * model.h, 
                        (self.s[1] + 0.5) * model.h))
        points.append(((self.r[0] + 0.5) * model.h,
                        (self.r[1] + 0.5) * model.h))
        points.sort()
        print(points)

        #Counting time of a ray arrival
        t_sum = 0
        for k in range(len(points) - 1):
            print(points[k], points[k + 1])
            s = math.sqrt((points[k + 1][0] - points[k][0]) ** 2
                        + (points[k + 1][1] - points[k][1]) ** 2)
            i = int((points[k + 1][0] + points[k][0])/2)
            j = int((points[k + 1][1] + points[k][1])/2)
            t_sum = t_sum + s / model[j, i]
            print(f'Segment = {s}; velocity = {model[j,i]} t_sum = {t_sum}')



############################### SCRIPT BEHAIVIOR #############################

if __name__ == '__main__':
    print(f'Supplied {len(sys.argv)} command line arguments.')
    for i, arg in enumerate(sys.argv):
        print(f'Command line argument {i}: {arg}')
    if len(sys.argv) == 5:
        s = (int(sys.argv[1]), int(sys.argv[2]))
        r = (int(sys.argv[3]), int(sys.argv[4]))
    else:
        s = (S[0], S[1])
        r = (R[0], R[1])
    ray = Ray2D(s, r)
    print(ray.t)
    print(TEST_MODEL)
    ray.trace(TEST_MODEL)
    print(f'Exiting script {__file__} without errors.')
    exit(0)

