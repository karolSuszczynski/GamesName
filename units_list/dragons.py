from units.base_unit import BaseUnit
from units.possible_action_map import AirbornActionMapGenerator
from units.attacks import get_claw_dragon_attack
from units.armors import get_green_dragon_armor
from units.resistance_types import grean_dragon_resistance

class BabyGreenDragon(BaseUnit):
    def __init__(self):
        super().__init__("img/baby_green_dragon.png", speed=3, hp=500, rest_ability=20, attack=get_claw_dragon_attack(20), reach=1,
                         MoveActionMapGenerator = AirbornActionMapGenerator,
                         armor=get_green_dragon_armor(0.25), resistance=grean_dragon_resistance)