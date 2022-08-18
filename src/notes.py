#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TomoHack/src/notes.py

"""Template script that follows a decent coding style (based on PEP8).
"""

################################### IMPORTS ##################################

# Python standard library imports
import sys

# Necessary packages (not a part of standard library)

# Project modules (in the same folder/repo)


############################### GLOBAL CONSTANTS #############################
__author__    = "Sergei Abramenkov"
__copyright__ = "Copyright 2022, NSU GeoHack"
__license__   = "MIT"
__version__   = "0.0.2"
__status__    = "Development"
__email__     = "s.abramenkov@nsu.ru"
__maintainer__ = "Sergei Abramenkov"
__credits__   = [
                "Darina Ilyuhina",
                "Martina Terskaya",
                "Kristina Potapova",
                "Vasiliy Potapov",
                "Sergei Abramenkov"
                ]

############################# CLASSES & FUNCTIONS ############################



############################### SCRIPT BEHAIVIOR #############################
if __name__ == '__main__':
    print(f'Supplied {len(sys.argv)} command line arguments.')
    for i, arg in enumerate(sys.argv):
        print(f'Command line argument {i}: {arg}')
    print(f'Exiting script {__file__} without errors.')
    exit(0)
