from tkinter import *
from PIL import Image, ImageTk
import numpy as np

class MainWindow(Canvas):
    def __init__(self, window):
        super().__init__(window)
        self.focus_set()
        self.bind("<Configure>", self.on_resize)
        self.bind("<Key>", self.callback_key)
        self.bind("<Button-1>", self.callback)
        self.bind("<Button-3>", self.callback3)
        self.pack(fill=BOTH, expand=YES)
        self.current_view = None
      
    def open_view(self, view):
        if self.current_view is not None:
            self.current_view.hide()
        self.current_view = view

        self.current_view.place(x=5, y=5, width=self.winfo_width()-10, height=self.winfo_height()-10)
        self.current_view.show()
        
        
    def on_resize(self, event):
        w = event.width
        h = event.height

        self.paint()
        self.current_view.place(x=5, y=5, width=w-10, height=h-10)

    def callback(self, event, right = False):
        if event:
            if self.current_view is not None:
                self.current_view.on_click(event.x-5, event.y-5, right=False)
            event = not event
        
            
    def callback3(self, event):
        if event:
            if self.current_view is not None:
                self.current_view.on_click(event.x-5, event.y-5, right=True)
            event = not event

    def callback_key(self, event):
        if event:
            if self.current_view is not None:
                self.current_view.on_key_click(event.char)
            event = not event
            
    def paint(self):
        self.delete("all")
        W = self.winfo_width() 
        H = self.winfo_height()
        self.create_rectangle(0, 0, W, H, fill="#000077")
            
