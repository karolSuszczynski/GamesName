from tkinter import *
from gui.i_view import IView

class AbstractSelectFromListView(IView):

    def __init__(self, main_window, list_of_items):
        super().__init__(main_window)
        
        self.list_of_items = list_of_items

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
            if rest < self.button_h and idx < len(self.list_of_items):
                self.on_button_click(idx)

            event = not event

    def on_button_click(self, id):
        raise RuntimeError("Not implememnted abstarct method on_button_click")

    def paint(self):
        self.delete("all")
        W = self.winfo_width() 
        H = self.winfo_height()

        self.create_rectangle(0, 0, W, H, fill="#007700")



        self.create_rectangle(self.button_x,
                              self.button_y0,
                              self.button_x + self.button_w,
                              self.button_y0 + (len(self.list_of_items)-1) * self.button_y_shift + self.button_h,
                              fill="#770000"
                              )
        for i, map in enumerate(self.list_of_items):
            x = self.button_x
            y = self.button_y0 + i * self.button_y_shift
            w = self.button_w
            h = self.button_h
            self.create_text(x + w/2, y + h/2,
                             fill="#776677", font="Times 20 italic bold",
                             anchor=CENTER,
                             text=map[0]
                            )

