from battle_maps.abstract_battle_map import AbstractBattleMap
from units_list import *
from squad import Squad
from numpy.random import randint


class CavalryDuelMap(AbstractBattleMap):
    BOARD_WIDTH = 16
    BOARD_HEIGT = 9
    def __init__(self):
        super().__init__(self.BOARD_WIDTH, self.BOARD_HEIGT)
        
    def _create_squads(self):
        return [Squad(1, "#0000b0"), Squad(2, "#ff0b03")]
        
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
        
    