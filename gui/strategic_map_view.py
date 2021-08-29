import tkinter
from PIL import Image, ImageTk
import numpy as np
from gui.i_view import IView
from battle_maps.battle_engine import BattleEngine


class StrategicMapView(IView):
    def __init__(self, main_window):
        super().__init__(main_window)

        img = Image.open("img/empty.png")
        img = img.resize((50, 50), Image.ANTIALIAS)
        self.empty_image = ImageTk.PhotoImage(img)

        self.battle_engine = BattleEngine(self.main_window)

    def set_strategic_map(self, strategic_map):
        self.battle_engine.set_battlefield(strategic_map)

    def button_callback(self, event, right=False):
        assert self.battle_engine.battlefield is not None
        if event:
            y = int(event.y / 60)
            x = int((event.x - 30 * (y % 2)) / 60)
            if x >= 0 and x < self.battle_engine.battlefield.W and y >= 0 and y < self.battle_engine.battlefield.H:
                self.battle_engine.cliked(x, y, right)
                self.paint()
            event = not event

    def callback_key(self, event):
        assert self.battle_engine.battlefield is not None
        if event:
            key = event.char
            event = not event
            print(key)

    def paint(self):
        assert self.battle_engine.battlefield is not None
        self.delete("all")
        W = self.winfo_width()
        H = self.winfo_height()
        self.create_rectangle(0, 0, W, H, fill="#172032")
        for y in range(self.battle_engine.battlefield.H):
            for x in range(self.battle_engine.battlefield.W):
                if self.battle_engine.action_map is not None:
                    action = self.battle_engine.action_map[y][x]
                    if action is not None:
                        color = {"move": "#779922", "attack": "#ff7788", "support": "#22ff77"}[action]
                        self.create_rectangle(-5 + x * 60 + 30 * (y % 2), -5 + y * 60,
                                              55 + x * 60 + 30 * (y % 2), 55 + y * 60,
                                              fill=color)
                unit = self.battle_engine.battlefield[y][x]
                if unit is None:
                    self.create_image(x * 60 + 30 * (y % 2), y * 60, anchor=tkinter.NW, image=self.empty_image)
                else:
                    self.create_image(x * 60 + 30 * (y % 2), y * 60, anchor=tkinter.NW, image=unit.image)
                    self.create_text(30 + x * 60 + 30 * (y % 2), 30 + y * 60, fill=unit.owner.color,
                                     font="Times 20 italic bold",
                                     text=str(int(np.round(unit.hp, 0))))
        current_unit = self.battle_engine.current_unit
        if current_unit is not None:
            x = current_unit.x
            y = current_unit.y
            x = 15 + x * 60 + 30 * (y % 2)
            y = 15 + y * 60
            self.create_oval(x, y, x + 20, y + 20, fill="#999933")

            params = current_unit.get_params()

            text = ""
            for i, param in enumerate(params):
                text += f"{param} : {params[param]}\n"
            self.create_text((self.battle_engine.battlefield.W + 2) * 60, 30,
                             fill=current_unit.owner.color,
                             font="Times 20 italic bold",
                             anchor=tkinter.NW,
                             text=text)

