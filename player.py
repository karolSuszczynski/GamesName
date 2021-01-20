from tkinter import *
from PIL import Image, ImageTk
import numpy as np

class Player:
    def __init__(self, id, color):
        self.id = id
        self.units = []
        self.color = color
    
    def get_units_count(self):
        return len(self.units)
    
    def get_living_units_count(self):
        result = 0;
        for unit in self.units:
            if unit.hp > 0:
                result += 1
        return result
        
    
    def add_unit(self, unit):
        self.units.append(unit)
        unit.owner = self
        