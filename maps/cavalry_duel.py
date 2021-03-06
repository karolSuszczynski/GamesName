from maps.abstract_map import AbstractMap
from units.units import *
from player import Player
from numpy.random import randint


class CavalryDuelMap(AbstractMap):
    BOARD_WIDTH = 16
    BOARD_HEIGT = 9
    def __init__(self):
        super().__init__(self.BOARD_WIDTH, self.BOARD_HEIGT)
        
    def _create_players(self):
        return [Player(1, "#0000b0"), Player(2, "#ff0b03")]
        
    def _create_all_units(self):
        return [[(1,1, Horseman()),
                (1,2, Cavalryman()),
                (1,3, Horseman()),
                (1,4, Cataphract()),
                (1,5, Horseman()),
                (1,6, Cavalryman())
                ],
                [(14,2, Horseman()),
                (14,3, Cavalryman()),
                (14,4, Horseman()),
                (14,5, Cataphract()),
                (14,6, Horseman()),
                (14,7, Cavalryman()),
                ]
               ]
        
    