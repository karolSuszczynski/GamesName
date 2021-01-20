from tkinter import *
from PIL import Image, ImageTk
import numpy as np

class IView(Canvas):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.bind("<Configure>", self.on_resize)

        self.bind("<Button-1>", self.button_callback)
        self.bind("<Button-3>", self.right_button_callback)

    def button_callback(self, event, right=False):
        print(f"uniplemented click on view{event.x} {event.y} {right}")

    def right_button_callback(self, event):
        self.button_callback(event, right=True)

    def on_resize(self, event):
        self.paint()

    def paint(self):
        pass

    def on_key_click(self, key):
        print(f"uniplemented on_keyboard_click '{key}'")
    
