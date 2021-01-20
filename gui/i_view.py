from tkinter import *
from PIL import Image, ImageTk
import numpy as np

class IView(Canvas):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.bind("<Configure>", self.on_resize)

    def show(self):
        self.itemconfigure(id, state='normal')
        self.paint()

    def hide(self):
        self.itemconfigure(id, state='hidden')

    def on_resize(self, event):
        self.paint()

    def paint(self):
        pass

    def on_click(self, x, y, right):
        print(f"unimlemented click {x} {y} {right}")

    def on_key_click(self, key):
        print(f"unimlemented on_key_click {key}")
    
