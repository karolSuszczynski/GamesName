from PIL import Image, ImageTk
from units.base_unit import BaseUnit
from units.unit_with_ammo import UnitWithAmmo
from units.possible_action_map import AirbornActionMapGenerator
from units.attacks import get_sword_attack
class Footman(BaseUnit):
    def __init__(self):
        super().__init__("img/footman.png", speed=1, hp=150, rest_ability=4, attack=get_sword_attack(10), reach=1)
        
class Axeman(BaseUnit):
    def __init__(self):
        super().__init__("img/axeman.png", speed=1, hp=100, rest_ability=4, attack=get_sword_attack(20), reach=1)
        
class Spearman(BaseUnit):
    def __init__(self):
        super().__init__("img/spearman.png", speed=1, hp=100, rest_ability=4, attack=get_sword_attack(10), reach=2)

class Horseman(BaseUnit):
    def __init__(self):
        super().__init__("img/horseman.png", speed=2, hp=100, rest_ability=4, attack=get_sword_attack(10), reach=1)
        
class Charlatan(BaseUnit):
    def __init__(self):
        super().__init__("img/charlatan.png", speed=1, hp=70, rest_ability=5, attack=get_sword_attack(2), reach=1, healing=5)

class Infantryman(BaseUnit):
    def __init__(self):
        super().__init__("img/infantryman.png", speed=1, hp=250, rest_ability=6, attack=get_sword_attack(10), reach=1)
     
class Bardicheman(BaseUnit):
    def __init__(self):
        super().__init__("img/bardicheman.png", speed=1, hp=100, rest_ability=6, attack=get_sword_attack(30), reach=1)
  
class Pikeman(BaseUnit):
    def __init__(self):
        super().__init__("img/pikeman.png", speed=1, hp=100, rest_ability=6, attack=get_sword_attack(10), reach=3)

class Cavalryman(BaseUnit):
    def __init__(self):
        super().__init__("img/cavalryman.png", speed=3, hp=100, rest_ability=6, attack=get_sword_attack(10), reach=1)
        
class Healer(BaseUnit):
    def __init__(self):
        super().__init__("img/healer.png", speed=1, hp=100, rest_ability=10, attack=get_sword_attack(5), reach=2, healing=10)

class Legionist(BaseUnit):
    def __init__(self):
        super().__init__("img/legionist.png", speed=1, hp=300, rest_ability=8, attack=get_sword_attack(15), reach=1)

class Halbeldier(BaseUnit):
    def __init__(self):
        super().__init__("img/halbeldier.png", speed=1, hp=175, rest_ability=8, attack=get_sword_attack(28), reach=2)

class Hoplite(BaseUnit):
    def __init__(self):
        super().__init__("img/hoplite.png", speed=1, hp=200, rest_ability=8, attack=get_sword_attack(15), reach=2)

class Cataphract(BaseUnit):
    def __init__(self):
        super().__init__("img/cataphract.png", speed=3, hp=175, rest_ability=8, attack=get_sword_attack(15), reach=1)
