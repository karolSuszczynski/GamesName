from units.base_unit import BaseUnit
from units.possible_action_map import AirbornActionMapGenerator
from units.attacks import get_sword_attack

class BabyGreenDragon(BaseUnit):
    def __init__(self):
        super().__init__("img/baby_green_dragon.png", speed=3, hp=500, rest_ability=20, attack=get_sword_attack(20), reach=1,
                         MoveActionMapGenerator = AirbornActionMapGenerator)