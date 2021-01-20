from tkinter import *
from PIL import Image, ImageTk
import numpy as np

from gui.select_battle_view import SelectBattleView
from gui.battle_view import BattleView
from gui.view_type import ViewType


class MainWindow(Canvas):
    def __init__(self, window):
        super().__init__(window)
        self.bind("<Configure>", self.on_resize)
        self.bind("<Key>", self.callback_key)
        self.pack(fill=BOTH, expand=YES)
        self.current_view = None

        self.views = {
            ViewType.SELECT_BATTLE_VIEW: SelectBattleView(self),
            ViewType.BATTLE_VIEW: BattleView(self),
        }

    def open_view(self, view_type: ViewType):
        if self.current_view is not None:
            self.current_view.place(x=-1, y=-1, width=0, height=0)
        self.current_view = self.views[view_type]

        self.current_view.place(x=5, y=5, width=self.winfo_width()-10, height=self.winfo_height()-10)
        self.focus_set()
        
    def on_resize(self, event):
        w = event.width
        h = event.height

        self.paint()
        self.current_view.place(x=5, y=5, width=w-10, height=h-10)

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
            
