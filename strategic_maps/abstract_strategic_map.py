from battle_maps.battlefield import Battlefield

class AbstractBattleMap():
    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height
        
    def get_battlefield(self):
        squads = self._create_squads()
        squads = squads[:2]
        battlefield = Battlefield(self.board_width, self.board_height, squads)
        
        for squad, units_for_one_squad in zip(squads, self._create_all_units()):
            for x, y, unit in units_for_one_squad:
                assert battlefield.grid[y][x] is None
                unit.set_location(battlefield, x, y)
                squad.add_unit(unit)
        return battlefield
        
    def _create_squads(self):
        assert False, "Missing implementation"
        
    def _create_all_units(self):
        assert False, "Missing implementation"