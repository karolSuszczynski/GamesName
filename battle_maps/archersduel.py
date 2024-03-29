from battle_maps.abstract_battle_map import AbstractBattleMap
from units_list import *
from squad import Squad
from numpy.random import randint


class ArchersDuelMap(AbstractBattleMap):
    BOARD_WIDTH = 16
    BOARD_HEIGT = 8
    def __init__(self):
        super().__init__(self.BOARD_WIDTH, self.BOARD_HEIGT)
        
    def _create_squads(self):
        return [Squad(1, "#0000b0"), Squad(2, "#ff0b03")]
        
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
        
    