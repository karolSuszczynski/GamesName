from battle_maps.abstract_battle_map import AbstractBattleMap
from units_list import *
from squad import Squad
from numpy.random import randint


class RandomMap(AbstractBattleMap):
    COMMON_UNITS_COUNT = 2
    BASIC_UNITS_COUNT = 3
    BETTER_UNITS_COUNT = 2
    BEST_UNITS_COUNT = 1

    UNITS_TYPES = [Peasant, Footman]
    UNITS_TYPES1 = [Footman, Axeman, Spearman, Horseman, Bowman, Charlatan]
    UNITS_TYPES2 = [Infantryman, Bardicheman, Pikeman, Cavalryman, Archer, Healer]
    UNITS_TYPES3 = [Legionist, Halbeldier, Hoplite, Cataphract, Xbowman, Catapult, Rifleman]
    def __init__(self, board_width, board_height, squad_count=2):
        super().__init__(board_width, board_height)
        self.squad_count = squad_count
        self.empty_field = []
        for y in range(board_height):
            self.empty_field.append([True] * board_width)
    def _create_squads(self):
        squads = [Squad(1, "#0000b0"), Squad(2, "#ff0b03"), Squad(3, "#00da00"), Squad(4, "#ffff00"), Squad(5, "#80007f"), Squad(6, "#ff2bff")]
        return squads[:self.squad_count]
        
    def _create_all_units(self):
        return [self.crete_units_for_one_squad() for _ in range(self.squad_count)]
        
    def crete_units_for_one_squad(self):
        result = []
        result += self.crete_uniots_from_one_type_group(self.COMMON_UNITS_COUNT, self.UNITS_TYPES)
        result += self.crete_uniots_from_one_type_group(self.BASIC_UNITS_COUNT, self.UNITS_TYPES1)
        result += self.crete_uniots_from_one_type_group(self.BETTER_UNITS_COUNT, self.UNITS_TYPES2)
        result += self.crete_uniots_from_one_type_group(self.BEST_UNITS_COUNT, self.UNITS_TYPES3)
        return result
    def crete_uniots_from_one_type_group(self, units_count, UNITS_TYPES):
        result = []
        current_units_count = 0        
        while current_units_count < units_count:
            x = randint(self.board_width)
            y = randint(self.board_height)
            if self.empty_field[y][x]:
                self.empty_field[y][x] = False
                current_units_count += 1
                result.append((x,y,UNITS_TYPES[randint(len(UNITS_TYPES))]()))
        return result
    