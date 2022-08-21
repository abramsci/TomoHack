#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TomoHack/src/ray_tracing.py

"""Template script that follows a decent coding style (based on PEP8).
"""

################################### IMPORTS ##################################

# Python standard library imports
import sys
import math
import numpy as np
import matplotlib

# Necessary packages (not a part of standard library)

# Project modules (in the same folder/repo)


############################### GLOBAL CONSTANTS #############################
__author__    = "Martina Terskaya, Darina Ilyukhina and Sergei Abramenkov"
__copyright__ = "Copyright 2022, NSU GeoHack"
__license__   = "MIT"
__version__   = "0.0.2"

############################# CLASSES & FUNCTIONS ############################








############################### SCRIPT BEHAIVIOR #############################

#Вводим координатную сетку
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
coords_velocities = []

for row in range(arr.shape[0]):
    coords_velocities.append([])
    for col in range(arr.shape[1]):
        coords_velocities[row].append((col+0.5,  -(row+0.5)))
print(coords_velocities)
        
# Сюда должны подставляться значения координат источника и приёмника
#(по идее, если самый верхний левый пиксель это (1:1), то от этого числа нужно отнять 0.5)

xs = 0.5
xr = 2.5
ys = -1.5
yr = -0.5

#для визуализации, которая не получилась
source = [xs, ys]
receiver = [xr, yr]
plt.grid(which='major')
plt.xlim([0, 3])  
plt.ylim([0, 3])

#Находим уравнение прямой
k = (ys - yr) / (xs - xr)
b = yr - k*xr
#y = k*x + b
print(f"y = {k}x + {b}")


#Здесь я пыталась задать граничные значения range, чтобы итерироваться только по пикселям, которые нам нужны
xmin = xs+0.5
xmax = xr-0.5


l = [] #пустой список для записи координат точек пересечения с гранями
for x in range(1,3):   #здесь range надо задать по индексам матрицы 
    if x % 1 == 0:
        y = k*x + b
        coords = tuple([x,y])
        l.append(coords) 

for y in range(-1,0):
    if y % 1 == 0:
        x = (y - b)/k
        coords = tuple([x,y])
        l.append(coords)

l.sort() #сортируем по возрастанию х
print(l)

for index in range(len(l)+1):
    #print(i[0], i[1])
    # длина вектора по координатам s = ((x1 - x2)**2 + (y1 - y2)**2)**0.5 





if __name__ == '__main__':
    print(f'Supplied {len(sys.argv)} command line arguments.')
    for i, arg in enumerate(sys.argv):
        print(f'Command line argument {i}: {arg}')
    print(f'Exiting script {__file__} without errors.')
    exit(0)
