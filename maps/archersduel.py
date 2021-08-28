from maps.abstract_map import AbstractMap
from units_list import *
from player import Player
from numpy.random import randint


class ArchersDuelMap(AbstractMap):
    BOARD_WIDTH = 16
    BOARD_HEIGT = 8
    def __init__(self):
        super().__init__(self.BOARD_WIDTH, self.BOARD_HEIGT)
        
    def _create_players(self):
        return [Player(1, "#0000b0"), Player(2, "#ff0b03")]
        
    def _create_all_units(self):
        return [[(1,1, Bowman()),
                (1,2, Archer()),
                (1,3, Bowman()),
                (3,2, Footman())
                ],
                [(14,4, Bowman()),
                (14,5, Archer()),
                (14,6, Bowman()),
                (12,5, Footman())
                ]
               ]
        
    