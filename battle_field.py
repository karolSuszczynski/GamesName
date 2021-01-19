from tkinter import *
from PIL import Image, ImageTk
import numpy as np

class Battlefield:
    def __init__(self, window, W, H, players):
        self.canvas = Canvas(window, width = 1300, height = 700)
        self.canvas.focus_set()
        self.canvas.bind("<Key>", self.callback_key)
        self.canvas.bind("<Button-1>", self.callback)
        self.canvas.bind("<Button-3>", self.callback3)
        self.canvas.pack()
    
        img = Image.open("img/empty.png")
        img = img.resize((50,50), Image.ANTIALIAS)
        self.empty_image = ImageTk.PhotoImage(img)

        self.W = W
        self.H = H
        self.grid = []
        for h in range(self.H):
            self.grid.append([None]*self.W)
            
        self.focus = None
        
        self.players = players
        self.next_units = None
        self.current_unit = None
        self.action_map = None
        
    def init_batle(self):
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
        for player in self.players:
            for unit in player.units:
                if unit.hp > 0:
                    self.next_units.append(unit)
        np.random.shuffle(self.next_units)
        
    def callback(self, event, right = False):
        y = int (event.y / 60)
        x = int((event.x -  30*(y%2)) / 60)
        if x >= 0 and x < self.W and y >= 0 and y < self.H:
            self.cliked(x,y, right)
            self.plot()
            
    def callback3(self, event):
        self.callback(event, right = True)

    def callback_key(self, event):
        if event:
            key = event.char
            event = not event
            print(key)
            
    def cliked(self, x,y, right):
        sx = self.current_unit.x
        sy = self.current_unit.y
        succes = False
        if self.grid[y][x] is None:
            succes = self.current_unit.try_move(x,y)
        else:
            if x == sx and y == sy:
                self.current_unit.rest()
                succes = True
            else:
                target = self.grid[y][x]
                if target.owner == self.current_unit.owner:
                    succes = self.current_unit.try_support_position(x,y)
                else:
                    succes = self.current_unit.try_attack_position(x,y, special=right)
        if succes:
            self.focus = None
            self.next_unit()
    
        
    def plot(self):
        self.canvas.delete("all")
        W = self.canvas.winfo_width() 
        H = self.canvas.winfo_height()
        self.canvas.create_rectangle(0, 0, W, H, fill="#172032")
        for y in range(self.H):
            for x in range(self.W):
                if self.action_map is not None:
                    action = self.action_map[y][x]
                    if action is not None:
                        color = { "move" : "#779922", "attack": "#ff7788", "support" : "#22ff77"}[action]
                        self.canvas.create_rectangle(-5 + x * 60 + 30*(y%2),-5 + y * 60,
                                                55 + x * 60 + 30*(y%2), 55 + y * 60,
                                                fill=color)
                unit = self.grid[y][x]
                if unit is None:
                    self.canvas.create_image( x * 60 + 30*(y%2), y * 60, anchor=NW, image=self.empty_image)
                else:
                    self.canvas.create_image( x * 60 + 30*(y%2), y * 60, anchor=NW, image=unit.image)
                    self.canvas.create_text(30+x * 60 + 30*(y%2),30+ y * 60,fill=unit.owner.color,font="Times 20 italic bold",
                        text=str(int(np.round(unit.hp,0))))
        if self.current_unit is not None:
            x = self.current_unit.x
            y = self.current_unit.y
            x = 15+x * 60 + 30*(y%2)
            y = 15+ y * 60
            self.canvas.create_oval(x,y,x+20,y+20,fill="#999933")
            
            params = self.current_unit.get_params()
            for i, param in enumerate(params):
                self.canvas.create_text((self.W+2) * 60,30+ i * 60,fill=self.current_unit.owner.color,font="Times 20 italic bold",
                        text=f"{param} : {params[param]}")
            