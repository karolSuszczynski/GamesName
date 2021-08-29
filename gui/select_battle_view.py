from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from gui.i_view import IView

from battle_maps.archersduel import ArchersDuelMap
from battle_maps.betterarmies import BetterArmiesMap
from battle_maps.marcelsmap import MarcelsMap
from battle_maps.army_vs_dragon import ArmyVsDragon
from gui.view_type import ViewType
from gui.abstract_select_from_list_view import AbstractSelectFromListView

class SelectBattleView(AbstractSelectFromListView):
    AVAILABLE_MAPS = [
        ("ArchersDuelMap", ArchersDuelMap()),
        ("BetterArmiesMap", BetterArmiesMap()),
        ("1 vs 1", MarcelsMap()),
        ("Army vs Dragon", ArmyVsDragon()),
    ]

    def __init__(self, main_window):
        super().__init__(main_window, self.AVAILABLE_MAPS)

    def on_button_click(self, id):
        map = self.AVAILABLE_MAPS[id]
        print(f"you clicked at {id} :   {map[0]}")

        battle_view = self.main_window.views[ViewType.BATTLE_VIEW]
        battle_view.set_battlefield(map[1].get_battlefield())
        self.main_window.open_view(ViewType.BATTLE_VIEW)