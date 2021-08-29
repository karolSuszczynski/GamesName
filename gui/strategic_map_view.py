import tkinter
from PIL import Image, ImageTk
import numpy as np
from gui.i_view import IView
from strategic_maps.strategic_engine import StrategicEngine


class StrategicMapView(IView):
    ground_height_color_map = \
        {
            0: "#0000ff",
            1: "#00ff00",
            2: "#aabbff",
            3: "#ff0000",
        }

    def __init__(self, main_window):
        super().__init__(main_window)

        img = Image.open("img/empty.png")
        img = img.resize((50, 50), Image.ANTIALIAS)
        self.empty_image = ImageTk.PhotoImage(img)

        self.strategic_engine = StrategicEngine(self.main_window)

    def set_startegicfield(self, startegicfield):
        assert startegicfield is not None
        self.strategic_engine.set_startegicfield(startegicfield)

    def button_callback(self, event, right=False):
        assert self.strategic_engine.startegicfield is not None
        if event:
            y = int(event.y / 60)
            x = int((event.x - 30 * (y % 2)) / 60)
            if x >= 0 and x < self.strategic_engine.battlefield.W and y >= 0 and y < self.strategic_engine.battlefield.H:
                self.strategic_engine.cliked(x, y, right)
                self.paint()
            event = not event

    def callback_key(self, event):
        assert self.strategic_engine.battlefield is not None
        if event:
            key = event.char
            event = not event
            print(key)

    def paint(self):
        assert self.strategic_engine.startegicfield is not None
        self.delete("all")
        W = self.winfo_width()
        H = self.winfo_height()
        self.create_rectangle(0, 0, W, H, fill="#172032")
        startegicfield = self.strategic_engine.startegicfield

        for item_y in range(startegicfield.H):
            for item_x in range(startegicfield.W):
                single_field = startegicfield[item_y][item_x]
                assert single_field is not None

                W = 60
                H = 60
                x = item_x * W + W * (item_y % 2) / 2
                y = item_y * H
                #self.create_image(x * 60 + 30 * (y % 2), y * 60, anchor=tkinter.NW, image=self.empty_image)
                self.create_rectangle(x, y, x+W, y+H,
                                      fill=self.ground_height_color_map[single_field.ground_height])
