import tkinter
from PIL import Image, ImageTk
import numpy as np
from gui.i_view import IView
from strategic_maps.startegicfield import Startegicfield
from gui.view_type import ViewType


class StrategicEngine:
    def __init__(self, main_window):
        self.startegicfield = None
        self.focus = None
        self.main_window = main_window
        
    def set_startegicfield(self, startegicfield):
        self.startegicfield = startegicfield

    def cliked(self, x,y, right):
        print(f"cliked {x} {y} {'right' if right else 'left'}")
            
    def check_winning_conditions(self):
        winner = None
        for squad in self.startegicfield.squads:
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
            self.main_window.open_view(ViewType.SELECT_strategic_VIEW)
            
        