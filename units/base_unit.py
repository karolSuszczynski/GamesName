from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from units.possible_action_map import LandMoveActionMap

def get_distance(x1,y1,x2,y2):
    y_distance = np.abs(y2 - y1)
    x1 += 0.5*(y1%2)
    x2 += 0.5*(y2%2)
    x_distance = np.abs(x2 - x1)
    x_distance -= y_distance*0.5
    if x_distance < 0:
        x_distance = 0
    return x_distance + y_distance

class BaseUnit:
    def __init__(self, image_path, speed, hp, rest_ability, attack, reach = 1, healing = 0, MoveActionMap = LandMoveActionMap):
        self.speed = speed
        self.max_hp = hp
        self.rest_ability = rest_ability
        self.attack = attack
        self.reach = reach
        self.healing = healing
        
        self.hp = hp
        self.current_attack = attack
    
        img = Image.open(image_path)
        img = img.resize((50,50), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(img)
        self.owner = None
        self.battlefield = None
        self.x = None
        self.y = None
        
        self.MoveActionMap = MoveActionMap
        self.move_action_map = None
    
    def get_params(self):
        return {"name": type(self).__name__,
        "speed" : self.speed,
        "hp" : f"{self.hp} / {self.max_hp}",
        "rest_ability" : self.rest_ability,
        "attack" : self.attack,
        "reach" : self.reach,
        "healing" : self.healing,
        }
        
    def get_action_map(self):
        action_map = self.move_action_map.get_action_map(self.speed, self.x, self.y)
        for y in range(self.battlefield.H):
            for x in range(self.battlefield.W):
                unit = self.battlefield.grid[y][x]
                if unit is not None:
                    if get_distance(self.x, self.y, x, y) <= self.reach:
                        if unit.owner != self.owner:
                            action_map[y][x] = "attack"
                        else:
                            action_map[y][x] = "support"
        return action_map
    
    def set_location(self, battlefield, x, y):
        self.battlefield = battlefield
        self.x = x
        self.y = y
        self.battlefield.grid[self.y][self.x] = self
        self.move_action_map = self.MoveActionMap(self.battlefield)
        
    def try_move(self,x,y):
        action_map = self.get_action_map()
        if action_map[y][x] != "move":
            return False
        self.battlefield.grid[self.y][self.x] = None
        self.x = x
        self.y = y
        self.battlefield.grid[self.y][self.x] = self
        return True
        
    def try_attack_position(self,x,y, special):
        if special:
            return False
        if get_distance(self.x, self.y, x, y) > self.reach:
            return False
        target = self.battlefield.grid[y][x]
        assert target is not None
        target.get_damaged(self.current_attack)
        return True
        
        
    def get_damaged(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.battlefield.grid[self.y][self.x] = None
    
    def try_support_position(self,x,y):
        if get_distance(self.x, self.y, x, y) > self.reach:
            return False
        if self.healing == 0:
            return False
        target = self.battlefield.grid[y][x]
        assert target is not None
        target.hp += self.healing
        return True
        
    def rest(self):
        self.hp += self.rest_ability
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        
    