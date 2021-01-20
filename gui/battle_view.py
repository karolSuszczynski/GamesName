import tkinter
from PIL import Image, ImageTk
import numpy as np
from gui.i_view import IView
from battlefield import Battlefield


class BattleView(IView):
    def __init__(self, main_window):
        super().__init__(main_window)
    
        img = Image.open("img/empty.png")
        img = img.resize((50,50), Image.ANTIALIAS)
        self.empty_image = ImageTk.PhotoImage(img)

        self.battlefield = None

        self.focus = None

        self.next_units = None
        self.current_unit = None
        self.action_map = None

    def set_battlefield(self, battlefield):
        self.battlefield = battlefield
        self.next_unit()
    
    def next_unit(self):
        if self.next_units is None or len(self.next_units) == 0:
            self.random_order()
        self.current_unit = self.next_units[0]
        self.action_map = self.current_unit.get_action_map()
        self.next_units = self.next_units[1:]
        if self.current_unit.hp <= 0:
            self.next_unit()
        
    def random_order(self):
        self.next_units = []
        for player in self.battlefield.players:
            for unit in player.units:
                if unit.hp > 0:
                    self.next_units.append(unit)
        np.random.shuffle(self.next_units)


    def button_callback(self, event, right = False):
        assert self.battlefield is not None
        if event:
            y = int (event.y / 60)
            x = int((event.x -  30*(y%2)) / 60)
            if x >= 0 and x < self.battlefield.W and y >= 0 and y < self.battlefield.H:
                self.cliked(x,y, right)
                self.paint()
            event = not event

    def callback_key(self, event):
        assert self.battlefield is not None
        if event:
            key = event.char
            event = not event
            print(key)
            
    def cliked(self, x,y, right):
        sx = self.current_unit.x
        sy = self.current_unit.y
        succes = False
        if self.battlefield[y][x] is None:
            succes = self.current_unit.try_move(x,y)
        else:
            if x == sx and y == sy:
                self.current_unit.rest()
                succes = True
            else:
                target = self.battlefield[y][x]
                if target.owner == self.current_unit.owner:
                    succes = self.current_unit.try_support_position(x,y)
                else:
                    succes = self.current_unit.try_attack_position(x,y, special=right)
        if succes:
            self.focus = None
            self.next_unit()
    
        
    def paint(self):
        assert self.battlefield is not None
        self.delete("all")
        W = self.winfo_width() 
        H = self.winfo_height()
        self.create_rectangle(0, 0, W, H, fill="#172032")
        for y in range(self.battlefield.H):
            for x in range(self.battlefield.W):
                if self.action_map is not None:
                    action = self.action_map[y][x]
                    if action is not None:
                        color = { "move" : "#779922", "attack": "#ff7788", "support" : "#22ff77"}[action]
                        self.create_rectangle(-5 + x * 60 + 30*(y%2),-5 + y * 60,
                                                55 + x * 60 + 30*(y%2), 55 + y * 60,
                                                fill=color)
                unit = self.battlefield[y][x]
                if unit is None:
                    self.create_image( x * 60 + 30*(y%2), y * 60, anchor=tkinter.NW, image=self.empty_image)
                else:
                    self.create_image( x * 60 + 30*(y%2), y * 60, anchor=tkinter.NW, image=unit.image)
                    self.create_text(30+x * 60 + 30*(y%2),30+ y * 60,fill=unit.owner.color,font="Times 20 italic bold",
                        text=str(int(np.round(unit.hp,0))))
        if self.current_unit is not None:
            x = self.current_unit.x
            y = self.current_unit.y
            x = 15+x * 60 + 30*(y%2)
            y = 15+ y * 60
            self.create_oval(x,y,x+20,y+20,fill="#999933")
            
            params = self.current_unit.get_params()
            for i, param in enumerate(params):
                self.create_text((self.battlefield.W+2) * 60,30+ i * 60,
                                 fill=self.current_unit.owner.color,
                                 font="Times 20 italic bold",
                                 anchor=tkinter.W,
                                 text=f"{param} : {params[param]}")
            
