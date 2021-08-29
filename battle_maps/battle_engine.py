import tkinter
from PIL import Image, ImageTk
import numpy as np
from gui.i_view import IView
from battle_maps.battlefield import Battlefield
from gui.view_type import ViewType


class BattleEngine:
    def __init__(self, main_window):
        self.battlefield = None
        self.focus = None
        self.next_units = None
        self.current_unit = None
        self.action_map = None
        self.main_window = main_window
        
    def set_battlefield(self, battlefield):
        self.battlefield = battlefield
        self.next_units = None
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
        for squad in self.battlefield.squads:
            for unit in squad.units:
                if unit.hp > 0:
                    self.next_units.append(unit)
        np.random.shuffle(self.next_units)


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
                    self.check_winning_conditions()
        if succes:
            self.focus = None
            self.next_unit()
            
    def check_winning_conditions(self):
        winner = None
        for squad in self.battlefield.squads:
            living_units_count = squad.get_living_units_count()
            if living_units_count > 0:
                if winner is None:
                    winner = squad
                else:
                    return
        if winner is None:
            print("Nobody has any units")
        else:
            print(f"{squad.id} won")
            self.main_window.open_view(ViewType.SELECT_BATTLE_VIEW)
            
        