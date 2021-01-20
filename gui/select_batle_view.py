from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from gui.i_view import IView

class SelectBatleView(IView):
    def __init__(self, main_window):
        super().__init__(main_window)

    def paint(self):
        self.delete("all")
        W = self.winfo_width() 
        H = self.winfo_height()

        self.create_rectangle(0, 0, W, H, fill="#ff1133")
