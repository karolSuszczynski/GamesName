from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from gui.i_view import IView

from maps.archersduel import ArchersDuelMap
from maps.betterarmies import BetterArmiesMap
from maps.marcelsmap import MarcelsMap
from maps.army_vs_dragon import ArmyVsDragon
from gui.view_type import ViewType

class SelectBattleView(IView):
    AVAILABLE_MAPS = [
        ("ArchersDuelMap", ArchersDuelMap()),
        ("BetterArmiesMap", BetterArmiesMap()),
        ("1 vs 1", MarcelsMap()),
        ("Army vs Dragon", ArmyVsDragon()),
    ]

    def __init__(self, main_window):
        super().__init__(main_window)

        self.button_x = 200
        self.button_y0 = 50
        self.button_y_shift = 150
        self.button_w = 400
        self.button_h = 60

    def button_callback(self, event, right = False):
        if event:
            x = event.x
            y = event.y

            y -= self.button_y0
            idx = int(y / self.button_y_shift)
            rest = y - idx * self.button_y_shift
            if rest < self.button_h and idx < len(self.AVAILABLE_MAPS):
                self.on_butyon_click(idx)

            event = not event

    def on_butyon_click(self, id):
        map = self.AVAILABLE_MAPS[id]
        print(f"you clicked at {id} :   {map[0]}")

        battle_view = self.main_window.views[ViewType.BATTLE_VIEW]
        battle_view.set_battlefield(map[1].get_battlefield())
        self.main_window.open_view(ViewType.BATTLE_VIEW)


    def paint(self):
        self.delete("all")
        W = self.winfo_width() 
        H = self.winfo_height()

        self.create_rectangle(0, 0, W, H, fill="#007700")



        self.create_rectangle(self.button_x,
                              self.button_y0,
                              self.button_x + self.button_w,
                              self.button_y0 + (len(self.AVAILABLE_MAPS)-1) * self.button_y_shift + self.button_h,
                              fill="#770000"
                              )
        for i, map in enumerate(self.AVAILABLE_MAPS):
            x = self.button_x
            y = self.button_y0 + i * self.button_y_shift
            w = self.button_w
            h = self.button_h
            #self.create_rectangle(x, y, x + w, y + h, fill="#770000")
            self.create_text(x + w/2, y + h/2,
                             fill="#776677", font="Times 20 italic bold",
                             anchor=CENTER,
                             text=map[0]
                            )

