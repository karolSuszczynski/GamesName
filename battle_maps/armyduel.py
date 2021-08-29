from battle_maps.abstract_battle_map import AbstractBattleMap
from units_list import *
from squad import Squad
from numpy.random import randint


class ArmyDuelMap(AbstractBattleMap):
    BOARD_WIDTH = 16
    BOARD_HEIGT = 11
    def __init__(self):
        super().__init__(self.BOARD_WIDTH, self.BOARD_HEIGT)
        
    def _create_squads(self):
        return [Squad(1, "#0000b0"), Squad(2, "#ff0b03")]
        
    def _create_all_units(self):
        return [[(1,1, Footman()),
                (1,2, Spearman()),
                (1,3, Axeman()),
                (0,2, Bowman()),
                (1,4, Spearman()),
                (0,4, Bowman()),
                (1,5, Axeman())
                ],
                [(13,1, Footman()),
                (14,2, Spearman()),
                (13,3, Axeman()),
                (15,2, Bowman()),
                (14,4, Spearman()),
                (15,4, Bowman()),
                (13,5, Axeman())
                ]
               ]
        
    