from tkinter import *
from PIL import Image, ImageTk
import numpy as np

class AbstractActionMap:
    
    def __init__(self, battlefield):
        self.battlefield = battlefield
        self.grid = battlefield.grid
        
    def get_neighbour(self, x, y):
        x += 0.5*(y%2)
        neighbour = [(x-0.5, y+1), (x+0.5, y+1), (x-1, y), (x+1, y), (x-0.5, y-1), (x+0.5, y-1)]
        neighbour = [(int(x), int(y)) for x, y in neighbour if x >= 0 and y >= 0]
        neighbour = [(x, y) for x, y in neighbour if x < self.battlefield.W and y < self.battlefield.H]
        return neighbour
        
    def get_action_map(self, unit_spped, start_x, start_y):
        action_map = []
        for y in range(self.battlefield.H):
            action_map.append([None]*self.battlefield.W)
        filed_for_check = self.get_neighbour(start_x,start_y)
        while unit_spped > 0:
            unit_spped -= 1
            new_filed_for_check = []
            for x,y in filed_for_check:
                if action_map[y][x] is not None:
                    continue
                if self.grid[y][x] is None:
                    action_map[y][x] = "move"
                if self.can_go_throw(x,y):
                    new_filed_for_check += self.get_neighbour(x,y)
            filed_for_check = new_filed_for_check
        return action_map
          
    def can_go_throw(self, x, y):
        assert False, "Not implemented abstract nethod"
        
class LandMoveActionMap(AbstractActionMap):
    def can_go_throw(self, x, y):
        if self.grid[y][x] is None:
            return True
        return False
                
        