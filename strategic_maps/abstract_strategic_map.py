from strategic_maps.startegicfield import Startegicfield

class AbstractStrategicMap():
    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height
        
    def get_startegicfield(self):
        players = self._create_players()
        startegicfield = Startegicfield(self.board_width, self.board_height, players)
        return self._fill_startegicfield(startegicfield)

    def _create_players(self):
        assert False, "Missing implementation"

    def _fill_startegicfield(self, startegicfield):
        assert False, "Missing implementation"