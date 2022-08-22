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
from skimage.draw import line
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

CANVAS_XSIZE = 384
CANVAS_YSIZE = 384

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
        self.background_image = Image.open('tst\\vulkano.jpg')
        self.background_image = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Add labels of models
        self.right_label = tk.Label()
        self.right_label.place(x=700, rely=0.35, width=300, height=300)

        self.left_label = tk.Label()
        self.left_label.place(relx=0, rely=0.35, width=300, height=300)

        # Variables of class instance
        self.stop = False

        # Button for selecting image via standard OS dialog
        self.button_load = tk.Button(text="Load from IMAGE",
                                     command=self.load_image,
                                     bg='lightgreen', fg = 'green')
        self.button_load.place(relwidth=0.103, relheight=0.05)

        # Button about add sources
        self.button_source = tk.Button(text='Add SOURCES',
                                       command=self.add_sources,
                                       bg='pink', fg = 'red')
        self.button_source.place(relwidth=0.103, relheight=0.05, rely=0.055)

        # Button about add sources
        self.button_receiver = tk.Button(text='Add RECEIVERS',
                                         command=self.add_receivers,
                                         bg='lightblue', fg = 'blue')
        self.button_receiver.place(relwidth=0.103, relheight=0.05, rely=0.11)

        # Button about stop process
        self.button_stop = tk.Button(text='STOP',
                                     command=self.stop_process,
                                     bg='red', fg = 'white')
        self.button_stop.place(relwidth=0.103, relheight=0.05, rely=0.165)

        # Button to connect points of sources and receivers
        self.button_to_connect = tk.Button(text='CONNECT POINTS',
                                           command=self.connect_points,
                                           bg='purple', fg = 'white')
        self.button_to_connect.place(relwidth=0.103, relheight=0.05, rely=0.22)

        # Button to clear canvas
        self.button_to_clear = tk.Button(text='CLEAR',
                                          command=self.clear_canvas,
                                           bg='black', fg = 'white')
        self.button_to_clear.place(relwidth=0.103, relheight=0.05, rely=0.275)

        # Button to craete massive sources
        self.button_to_mass_sources = tk.Button(text='Mass SOURCES',
                                                command=self.draw_mass_sources,
                                                bg='pink', fg = 'red')
        self.button_to_mass_sources.place(relwidth=0.103, relheight=0.05, relx=0.33, rely=0.055)

        # Button to create massive receivers
        self.button_to_mass_receivers = tk.Button(text='Mass RECEIVERS',
                                                command=self.draw_mass_receivers,
                                                bg='lightblue', fg='blue')
        self.button_to_mass_receivers.place(relwidth=0.103, relheight=0.05, relx=0.33, rely=0.11)

        # Entries for coords of draw lines
        self.x_start = tk.IntVar()
        self.x_end = tk.IntVar()
        self.y_start = tk.IntVar()
        self.y_end = tk.IntVar()
        self.step = tk.IntVar()

        self.label_x_start_end = tk.Label(text='X start/end:')
        self.label_x_start_end.place(relwidth=0.1, relheight=0.05, relx=0.105, rely=0.055)
        self.label_slesh_x = tk.Label(text='/')
        self.label_slesh_x.place(relwidth=0.01, relheight=0.05, relx=0.265, rely=0.055)
        self.label_y_start_end = tk.Label(text='Y start/end:')
        self.label_y_start_end.place(relwidth=0.1, relheight=0.05, relx=0.105, rely=0.11)
        self.label_slesh_y = tk.Label(text='/')
        self.label_slesh_y.place(relwidth=0.01, relheight=0.05, relx=0.265, rely=0.11)
        self.label_step = tk.Label(text='STEP:')
        self.label_step.place(relwidth=0.1, relheight=0.05, relx=0.105, rely=0.165)

        self.x_start_entry = tk.Entry(textvariable=self.x_start)
        self.x_end_entry = tk.Entry(textvariable=self.x_end)
        self.y_start_entry = tk.Entry(textvariable=self.y_start)
        self.y_end_entry = tk.Entry(textvariable=self.y_end)
        self.step_entry = tk.Entry(textvariable=self.step)

        self.x_start_entry.place(relwidth=0.05, relheight=0.05, relx=0.215, rely=0.055)
        self.x_end_entry.place(relwidth=0.05, relheight=0.05, relx=0.275, rely=0.055)
        self.y_start_entry.place(relwidth=0.05, relheight=0.05, relx=0.215, rely=0.11)
        self.y_end_entry.place(relwidth=0.05, relheight=0.05, relx=0.275, rely=0.11)
        self.step_entry.place(relwidth=0.05, relheight=0.05, relx=0.215, rely=0.165)

        # Canvas for visualization
        self.canvas_sint_model = tk.Canvas(width=CANVAS_XSIZE, height=CANVAS_YSIZE, bd=0, highlightthickness=0)
        self.canvas_sint_model.pack(expand=tk.YES)

        self.create_grid()

    def create_grid(self):
        for i in range(0,CANVAS_XSIZE, 12):
            self.canvas_sint_model.create_line(i, 0, i, CANVAS_YSIZE)
            self.canvas_sint_model.create_line(0, i, CANVAS_XSIZE, i)

    def clear_canvas(self):
        self.canvas_sint_model.delete('all')
        LIST_SOURCES.clear()
        LIST_RECEIVERS.clear()
        self.sources.clear()
        self.receivers.clear()
        
    def connect_points(self):
        for i in self.sources:
            for j in self.receivers:
                self.canvas_sint_model.create_line(i[0], i[1], j[0], j[1], fill='purple')
        for i in range(len(self.sources)):
            self.canvas_sint_model.create_rectangle((self.sources[i][0], self.sources[i][1])*2,
                                                    width=4, outline='red')
        for i in range(len(self.receivers)):
            self.canvas_sint_model.create_rectangle((self.receivers[i][0], self.receivers[i][1])*2,
                                                    width=4, outline='blue')

    def draw_mass_sources(self):
        xy_start, xy_end = line(self.x_start.get(), self.y_start.get(),
                                self.x_end.get(), self.y_end.get())
        mass_points = list(zip(xy_start, xy_end))
        for i in range(0, len(mass_points), self.step.get()):
            self.canvas_sint_model.create_rectangle((mass_points[i][0]*12+6,
                                                     mass_points[i][1]*12+6)*2,
                                                    width=4, outline='red')
            LIST_SOURCES.add(mass_points[i])

    def draw_mass_receivers(self):
        xy_start, xy_end = line(self.x_start.get(), self.y_start.get(),
                                self.x_end.get(), self.y_end.get())
        mass_points = list(zip(xy_start, xy_end))
        for i in range(0, len(mass_points), self.step.get()):
            self.canvas_sint_model.create_rectangle((mass_points[i][0]*12+6,
                                                     mass_points[i][1]*12+6)*2,
                                                    width=4, outline='blue')
            LIST_RECEIVERS.add(mass_points[i])

    def stop_process(self):
        self.stop = True
        self.sources = sorted(map(lambda x: (x[0]*12+6, x[1]*12+6), LIST_SOURCES),
                              key=lambda i: i[0])
        self.receivers = sorted(map(lambda x: (x[0]*12+6, x[1]*12+6), LIST_RECEIVERS),
                                key=lambda i: i[0])
        sorted(LIST_SOURCES, key=lambda i: i[0])
        sorted(LIST_RECEIVERS, key=lambda i: i[0])
        print(f'LIST_SOURCES: {LIST_SOURCES}\n'+
              f'LIST_RECEIVERS: {LIST_RECEIVERS}')

        # Draw lines between sources
        for i in range(len(self.sources)-1):
            self.canvas_sint_model.create_line(self.sources[i][0], self.sources[i][1],
                                               self.sources[i+1][0], self.sources[i+1][1],
                                               fill='pink')
            self.canvas_sint_model.create_rectangle((self.sources[i][0], self.sources[i][1])*2,
                                                    width=4, outline='red')
        # Draw lines between receivers
        for i in range(len(self.receivers)-1):
            self.canvas_sint_model.create_line(self.receivers[i][0], self.receivers[i][1],
                                               self.receivers[i+1][0], self.receivers[i+1][1],
                                               fill='lightblue')
            self.canvas_sint_model.create_rectangle((self.receivers[i][0], self.receivers[i][1])*2,
                                                    width=4, outline='blue')


    def callback(self, event):
        x = int(event.x / 12) * 12 + 6
        y = int(event.y / 12) * 12 + 6
        if self.flag == 'source':
            LIST_SOURCES.add((int((x-6)/12), int((y-6)/12)))
            self.canvas_sint_model.create_rectangle((x, y)*2, width=4, outline='red')
        else:
            LIST_RECEIVERS.add((int((x-6)/12), int((y-6)/12)))
            self.canvas_sint_model.create_rectangle((x, y)*2, width=4, outline='blue')

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

                self.left_image = self.original_image.resize((300, 300), Image.Resampling.LANCZOS)
                self.left_image = ImageTk.PhotoImage(self.left_image)
                self.left_label = tk.Label(image=self.left_image)
                self.left_label.place(relx=0, rely=0.35, width=300, height=300)

                self.resize_image = self.original_image.resize((32, 32), Image.Resampling.LANCZOS)
                self.resize_image = self.resize_image.resize((CANVAS_XSIZE, CANVAS_YSIZE), Image.NEAREST)
                (self.img_width, self.img_height) = self.resize_image.size
                self.canvas_sint_model.config(width=self.img_width, height=self.img_height)
                self.thumbnail = ImageTk.PhotoImage(self.resize_image)
                self.canvas_sint_model.create_image(0, 0, image=self.thumbnail,
                                                anchor=tk.NW)
                self.create_grid()

        except FileNotFoundError:
            pass
        return image_path

    def run(self):
        self.mainloop()


############################### SCRIPT BEHAIVIOR #############################
if __name__ == '__main__':
    app = Window()
    app.run()
