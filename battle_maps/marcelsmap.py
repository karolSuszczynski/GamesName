from battle_maps.abstract_battle_map import AbstractBattleMap
from units_list import *
from squad import Squad
from numpy.random import randint


class MarcelsMap(AbstractBattleMap):
    BOARD_WIDTH = 15
    BOARD_HEIGT = 10
    def __init__(self):
        super().__init__(self.BOARD_WIDTH, self.BOARD_HEIGT)
        
    def _create_squads(self):
        return [Squad(1, "#0000b0"), Squad(2, "#ff0b03")]
        
    def _create_all_units(self):
        return [[(1,1, Footman())
                ],
                [(1,5, Axeman())
                ]
               ]
        
    