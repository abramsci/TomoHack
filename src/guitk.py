#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TomoHack/src/guitk.py

"""Graphical user interface for working with blocks of tomography.

Module is based on tkinter framework (inculeded in Python standard library).
Python Image Library (PIL) is used for picture reading and drawing.
"""
################################### IMPORTS ##################################

# Python standard library imports
import tkinter as tk
from tkinter.filedialog import askopenfilename
import msvcrt
# Necessary packages
from PIL import Image, ImageTk

# Project modules
import velocity_model
from notes import __status__, __email__, __maintainer__, __credits__


############################### GLOBAL CONSTANTS #############################
__author__    = "Vasiliy Potapov, Kristina Potapova and Sergei Abramenkov"
__copyright__ = "Copyright 2022, NSU GeoHack"
__license__   = "MIT"
__version__   = "0.0.2"

# Main window dimensions
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

CANVAS_XSIZE = 600
CANVAS_YSIZE = 600

LIST_SOURCES = []
LIST_RECEIVERS = []

############################# CLASSES & FUNCTIONS ############################

"""Root class for the application - main window inhereting from Tk class.

Attributes (additional to Tk class):

"""
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('TomoHack GUI')
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.configure(bg='lightgreen')

        # Button for selecting image via standard OS dialog
        self.button_load = tk.Button(text="Load from image", 
                                    command=self.load_image)
        self.button_load.place(relwidth=0.15, relheight=0.1)

        self.button_source = tk.Button(text='Add sources',
                                       command=self.add_sources)
        self.button_source.place(relwidth=0.15, relheight=0.1, rely=0.105)
        # Canvas for visualization

        self.canvas_sint_model = tk.Canvas(width=CANVAS_XSIZE, height=CANVAS_YSIZE)
        #self.canvas_sint_model.bind('<Button-1>', self.callback)
        self.canvas_sint_model.pack(expand=tk.YES)

    def callback(self, event):
        LIST_SOURCES.append((event.x, event.y))

    def add_sources(self):
        self.canvas_sint_model.bind('<Button-1>', self.callback)
        print(LIST_SOURCES)

    def load_image(self):
        """Load an image as a model via OS standard file choosing menu.
        """
        try:
            image_path = askopenfilename(
                                parent=self,
                                title='Choose file',
                                filetypes=[('Image Files', 
                                ['.jpeg', '.jpg', '.png', '.bmp'])]
                                )
            print(image_path)
            if image_path:

                self.original_image = Image.open(image_path)
                (self.img_width, self.img_height) = self.original_image.size
                self.canvas_sint_model.config(width=self.img_width, height=self.img_height)
                self.thumbnail = ImageTk.PhotoImage(self.original_image)
                self.canvas_sint_model.create_image(0, 0, image=self.thumbnail,
                                                anchor=tk.NW)

                
        except FileNotFoundError:
            pass
        return image_path

    def run(self):
        self.mainloop()


############################### SCRIPT BEHAIVIOR #############################
if __name__ == '__main__':
    app = Window()
    app.run()
