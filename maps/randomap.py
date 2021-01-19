from maps.abstract_map import AbstractMap
from units.units import *
from player import Player
from numpy.random import randint


class RandomMap(AbstractMap):
    COMMON_UNITS_COUNT = 2
    BASIC_UNITS_COUNT = 3
    BETTER_UNITS_COUNT = 2
    BEST_UNITS_COUNT = 1

    UNITS_TYPES = [Peasant, Footman]
    UNITS_TYPES1 = [Footman, Axeman, Spearman, Horseman, Bowman, Charlatan]
    UNITS_TYPES2 = [Infantryman, Bardicheman, Pikeman, Cavalryman, Archer, Healer]
    UNITS_TYPES3 = [Legionist, Halbeldier, Hoplite, Cataphract, Xbowman, Catapult, Rifleman]
    def __init__(self, board_width, board_height, player_count=2):
        super().__init__(board_width, board_height)
        self.player_count = player_count
        self.empty_field = []
        for y in range(board_height):
            self.empty_field.append([True] * board_width)
    def _create_players(self):
        players = [Player(1, "#0000b0"), Player(2, "#ff0b03"), Player(3, "#00da00"), Player(4, "#ffff00"), Player(5, "#80007f"), Player(6, "#ff2bff")]
        return players[:self.player_count]
        
    def _create_all_units(self):
        return [self.crete_units_for_one_player() for _ in range(self.player_count)]
        
    def crete_units_for_one_player(self):
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
    