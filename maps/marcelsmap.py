from maps.abstract_map import AbstractMap
from units.units import *
from player import Player
from numpy.random import randint


class MarcelsMap(AbstractMap):
    BOARD_WIDTH = 15
    BOARD_HEIGT = 10
    def __init__(self):
        super().__init__(self.BOARD_WIDTH, self.BOARD_HEIGT)
        
    def _create_players(self):
        return [Player(1, "#0000b0"), Player(2, "#ff0b03")]
        
    def _create_all_units(self):
        return [[(1,1, Footman())
                ],
                [(1,5, Axeman())
                ]
               ]
        
    