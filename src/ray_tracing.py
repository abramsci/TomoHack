#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TomoHack/src/ray_tracing.py

"""...
"""

################################### IMPORTS ##################################

# Python standard library imports
import sys
import math
import numpy as np

# Necessary packages (not a part of standard library)
from matplotlib import pyplot as plt

# Project modules (in the same folder/repo)
from notes import __status__, __email__, __maintainer__, __credits__

############################### GLOBAL CONSTANTS #############################
__author__    = "Martina Terskaya, Darina Ilyukhina and Sergei Abramenkov"
__copyright__ = "Copyright 2022, NSU GeoHack"
__license__   = "MIT"
__version__   = "0.0.2"

############################# CLASSES & FUNCTIONS ############################

velmod = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
h = 1.0

source = (0, 1)
receiver = (2, 0)


Class Ray2D()
    def __init__(self, source, receiver):
        self.time = None
        self.source
        self.receiver
        
    

def trace(self, velmod):
    # Obtaining straight line equation
    a = (source[1] - receiver[1]) / (source[0] - receiver[0])
    b = h * (source[1] + 0.5 - a * (source[0] + 0.5))
    print(f"y = {a}x + {b}")
    print(f"x = (y - {b}) / {a}")

    # Looking for points on block edges
    points = []
    i_start = min(source[0], receiver[0]) + 1
    i_end = max(source[0], receiver[0]) + 1
    for i in range(i_start, i_end):
        points.append((i * h, a * i * h + b))
    j_start = min(source[1], receiver[1]) + 1
    j_end = max(source[1], receiver[1]) + 1
    for j in range(j_start, j_end):
        points.append(((j * h - b) / a , j * h))

    points.append(((source[0] + 0.5) * h, (source[1] + 0.5) * h))
    points.append(((receiver[0] + 0.5) * h, (receiver[1] + 0.5) * h))
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
        t_sum = t_sum + s / velmod[i, j]
        print(f'Segment distance = {s}; velocity = {velmod[i,j]} t_sum = {t_sum}')



############################### SCRIPT BEHAIVIOR #############################

if __name__ == '__main__':
    print(f'Supplied {len(sys.argv)} command line arguments.')
    for i, arg in enumerate(sys.argv):
        print(f'Command line argument {i}: {arg}')
    print(f'Exiting script {__file__} without errors.')
    exit(0)

