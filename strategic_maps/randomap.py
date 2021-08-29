from strategic_maps.abstract_strategic_map import AbstractStrategicMap
from strategic_maps.startegicfield import Startegicfield
from player import Player
from numpy.random import randint


class RandomMap(AbstractStrategicMap):

    def __init__(self, board_width, board_height, squad_count=2):
        super().__init__(board_width, board_height)
        self.squad_count = squad_count

    def _create_players(self):
        squads = [Player(1, "#0000b0"), Player(2, "#ff0b03"), Player(3, "#00da00"), Player(4, "#ffff00"),
                  Player(5, "#80007f"), Player(6, "#ff2bff")]
        return squads[:self.squad_count]

    def _fill_startegicfield(self, startegicfield: Startegicfield):
        for y in range(startegicfield.H):
            for x in range(startegicfield.W):
                startegicfield.grid[y][x].ground_height = randint(4)
        return startegicfield