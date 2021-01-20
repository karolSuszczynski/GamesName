from maps.abstract_map import AbstractMap
from units.units import *
from player import Player
from numpy.random import randint


class BetterArmiesMap(AbstractMap):
    BOARD_WIDTH = 16
    BOARD_HEIGHT = 11
    def __init__(self):
        super().__init__(self.BOARD_WIDTH, self.BOARD_HEIGHT)
        
    def _create_players(self):
        return [Player(1, "#0000b0"), Player(2, "#ff0b03")]
        
    def _create_all_units(self):
        return [[(0,0, Archer()),
                (0,1, Healer()),
                (0,2, Archer()),
                (0,3, Healer()),
                (0,4, Archer()),
                (0,5, Healer()),
                (1,0, Bardicheman()),
                (1,1, Bardicheman()),
                (1,2, Bardicheman()),
                (1,3, Bardicheman()),
                (1,4, Bardicheman()),
                (1,5, Bardicheman()),
                (2,0, Infantryman()),
                (2,2, Infantryman()),
                (2,4, Infantryman())
                ],
                [(15,0, Healer()),
                (15,1, Archer()),
                (15,2, Healer()),
                (15,3, Archer()),
                (15,4, Healer()),
                (15,5, Archer()),
                (14,0, Bardicheman()),
                (14,1, Bardicheman()),
                (14,2, Bardicheman()),
                (14,3, Bardicheman()),
                (14,4, Bardicheman()),
                (14,5, Bardicheman()),
                (13,1, Infantryman()),
                (13,3, Infantryman()),
                (13,5, Infantryman())
                ]
               ]
        
    
