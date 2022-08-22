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

CANVAS_XSIZE = 400
CANVAS_YSIZE = 400

LIST_SOURCES = set()
LIST_RECEIVERS = set()

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

        # Variables of class instance
        self.stop = False

        # Button for selecting image via standard OS dialog
        self.button_load = tk.Button(text="Load from image", 
                                    command=self.load_image)
        self.button_load.place(relwidth=0.1, relheight=0.05)

        # Button about add sources
        self.button_source = tk.Button(text='Add sources',
                                       command=self.add_sources)
        self.button_source.place(relwidth=0.1, relheight=0.05, rely=0.055)

        # Button about add sources
        self.button_receiver = tk.Button(text='Add receivers',
                                       command=self.add_receivers)
        self.button_receiver.place(relwidth=0.1, relheight=0.05, rely=0.11)

        # Button about stop process
        self.button_stop = tk.Button(text='Stop',
                                     command=self.stop_process)
        self.button_stop.place(relwidth=0.1, relheight=0.05, rely=0.165)

        # Button to connect points of sources and receivers
        self.button_to_connect = tk.Button(text='connect points',
                                           command=self.connect_points)
        self.button_to_connect.place(relwidth=0.1, relheight=0.05, rely=0.22)

        # Entries for coords of draw lines
        self.x_start = tk.IntVar()
        self.x_end = tk.IntVar()
        self.y_start = tk.IntVar()
        self.y_end = tk.IntVar()

        self.label_x_start_end = tk.Button(text='X start/end:',
                                           command=self.draw_line_x)
        self.label_x_start_end.place(relwidth=0.1, relheight=0.05, relx=0.105, rely=0.055)
        self.label_slesh_x = tk.Label(text='/')
        self.label_slesh_x.place(relwidth=0.01, relheight=0.05, relx=0.265, rely=0.055)
        self.label_y_start_end = tk.Label(text='Y start/end:')
        self.label_y_start_end.place(relwidth=0.1, relheight=0.05, relx=0.105, rely=0.11)
        self.label_slesh_y = tk.Label(text='/')
        self.label_slesh_y.place(relwidth=0.01, relheight=0.05, relx=0.265, rely=0.11)


        self.x_start_entry = tk.Entry(textvariable=self.x_start)
        self.x_end_entry = tk.Entry(textvariable=self.x_end)
        self.y_start_entry = tk.Entry(textvariable=self.y_start)
        self.y_end_entry = tk.Entry(textvariable=self.y_end)
        self.y_end_entry = tk.Entry(textvariable=self.y_end)

        self.x_start_entry.place(relwidth=0.05, relheight=0.05, relx=0.215, rely=0.055)
        self.x_end_entry.place(relwidth=0.05, relheight=0.05, relx=0.275, rely=0.055)
        self.y_start_entry.place(relwidth=0.05, relheight=0.05, relx=0.215, rely=0.11)
        self.y_end_entry.place(relwidth=0.05, relheight=0.05, relx=0.275, rely=0.11)
        # Canvas for visualization

        self.canvas_sint_model = tk.Canvas(width=CANVAS_XSIZE, height=CANVAS_YSIZE)
        self.canvas_sint_model.pack(expand=tk.YES)

    def connect_points(self):
        for i in range(len(self.sources)-1):
            self.canvas_sint_model.create_line(self.sources[i][0], self.sources[i][1],
                                               self.sources[i+1:i+2][0:1], self.sources[i+1:i+2][1:],
                                               fill='pink')
        for i in range(len(self.receivers)-1):
            self.canvas_sint_model.create_line(self.receivers[i][0], self.receivers[i][1],
                                               self.receivers[i+1][0], self.receivers[i+1][1],
                                               fill='lightblue')

    def draw_line_x(self):
        self.canvas_sint_model.create_line(self.x_start.get(), self.y_start.get(),
                                           self.x_end.get(), self.y_end.get(), fill='green')

    def stop_process(self):
        self.stop = True
        self.sources = sorted(LIST_SOURCES, key=lambda i: i[0])
        self.receivers = sorted(LIST_RECEIVERS, key=lambda i: i[0])
        print(f'LIST_SOURCES: {self.sources}\n'+
              f'LIST_RECEIVERS: {self.receivers}')
        for i in range(len(self.sources)-1):
            self.canvas_sint_model.create_line(self.sources[i][0], self.sources[i][1],
                                               self.sources[i+1][0], self.sources[i+1][1],
                                               fill='pink')
        for i in range(len(self.receivers)-1):
            self.canvas_sint_model.create_line(self.receivers[i][0], self.receivers[i][1],
                                               self.receivers[i+1][0], self.receivers[i+1][1],
                                               fill='lightblue')

    def callback(self, event):
        if self.flag == 'source':
            LIST_SOURCES.add((event.x, event.y))
            self.canvas_sint_model.create_rectangle((event.x, event.y)*2, outline='red')
        else:
            LIST_RECEIVERS.add((event.x, event.y))
            self.canvas_sint_model.create_rectangle((event.x, event.y)*2, outline='blue')

    def add_sources(self):
        self.flag = 'source'
        self.canvas_sint_model.bind('<Button-1>', self.callback)
        if self.stop:
            self.stop = False
            self.canvas_sint_model.unbind('<Button-1>')
            return None

    def add_receivers(self):
        self.flag = 'receiver'
        self.canvas_sint_model.bind('<Button-1>', self.callback)
        if self.stop:
            self.stop = False
            self.canvas_sint_model.unbind('<Button-1>')
            return None

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
