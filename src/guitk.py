#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PycharmProjects\GeoHack\guitk.py

"""Graphical user interface for the seismic tomography program.
Graphical interface for working with the main blocks of tomography:
velocity model parameterization, ray tracing, linearization, matrix inversion, visualization.
"""
# import standard libraries
import os
from tkinter import Label, Button, Tk
import tkinter.filedialog as fd

from PIL import Image, ImageTk

# window dimensions
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

IMAGE_PATH = None

# Create a window gui
class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title('TomoHack')
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.configure(bg='lightgreen')
        #self.point_dict = {}

        # creating a block with the selected image
        self.pil_original = Image.new('RGB', (600, 600), 'lightgreen')
        self.pil_image = Image.new('RGB', (600, 600), 'lightgreen')
        self.tk_original = ImageTk.PhotoImage(self.pil_original)
        self.label_original = Label(self, image=self.tk_original)
        self.label_original.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)

        # image upload button
        self.button_load = Button(text="Load", command=self.load)
        self.button_load.place(relx=0.15, rely=0.0, relwidth=0.15, relheight=0.1)

    # load image file
    def load(self):
        try:
            IMAGE_PATH = fd.askopenfilename(parent=self, initialdir=os.getcwd(),
                                          title='Choose file',
                                          filetypes=[('Image Files', ['.jpeg', '.jpg', '.png', '.bmp'])])
            print(IMAGE_PATH)
            if IMAGE_PATH:
                self.pil_original = Image.open(IMAGE_PATH)
                self.tk_original = ImageTk.PhotoImage(self.pil_original)
                self.label_original.config(image=self.tk_original)
        except FileNotFoundError:
            pass

    # start create gui
    def run(self):
        self.mainloop()



if __name__ == '__main__':
    app = Window()
    app.run()
    #print(IMAGE_PATH)