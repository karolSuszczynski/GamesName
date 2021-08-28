from PIL import Image, ImageTk
from units.base_unit import BaseUnit
from units.unit_with_ammo import UnitWithAmmo
from units.possible_action_map import AirbornActionMapGenerator
from units.attacks import get_sword_attack

class Tower(UnitWithAmmo):
    def __init__(self):
        super().__init__("img/tower.png", speed=0, hp=999, rest_ability=0.75, attack=99, reach=1, healing=3, ammo=7, ammo_reach=5, ammo_attack=74)

