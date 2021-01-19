from battle_field import Battlefield

class AbstractMap():
    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height
        
    def get_battlefield(self, window):
        players = self._create_players()
        players = players[:2]
        battlefield = Battlefield(window, self.board_width, self.board_height, players)
        
        for player, units_for_one_player in zip(players, self._create_all_units()):
            for x, y, unit in units_for_one_player:
                assert battlefield.grid[y][x] is None
                unit.set_location(battlefield, x, y)
                player.add_unit(unit)
        return battlefield
        
    def _create_players(self):
        assert False, "Missing implementation"
        
    def _create_all_units(self):
        assert False, "Missing implementation"