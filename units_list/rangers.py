from PIL import Image, ImageTk
from units.base_unit import BaseUnit
from units.unit_with_ammo import UnitWithAmmo
from units.possible_action_map import AirbornActionMapGenerator
from units.attacks import get_sword_attack


class Peasant(UnitWithAmmo):
    def __init__(self):
        super().__init__("img/peasant.png", speed=1, hp=77, rest_ability=4, attack=10, reach=1, healing=0, ammo=1, ammo_reach=4, ammo_attack=299) 
        
    def try_attack_position(self,x,y,special):
        result = super().try_attack_position(x,y,special)
        if self.ammo == 0:
            self.current_attack=8
            image_path="img/hick.png"
            img = Image.open(image_path)
            img = img.resize((50,50), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(img)
        return result

        
class Bowman(UnitWithAmmo):
    def __init__(self):
        super().__init__("img/bowman.png", speed=1, hp=50, rest_ability=4, attack=5, reach=1, healing=0, ammo=12, ammo_reach=5, ammo_attack=10)    
        
class Archer(UnitWithAmmo):
    def __init__(self):
        super().__init__("img/archer.png", speed=1, hp=50, rest_ability=6, attack=7, reach=1, healing=0, ammo=18, ammo_reach=6, ammo_attack=12)


class Xbowman(UnitWithAmmo):
    def __init__(self):
        super().__init__("img/xbowman.png", speed=1, hp=75, rest_ability=8, attack=8, reach=1, healing=0, ammo=20, ammo_reach=6, ammo_attack=20)

class Rifleman(UnitWithAmmo):
    def __init__(self):
        super().__init__("img/rifleman.png", speed=2, hp=75, rest_ability=9, attack=8, reach=1, healing=1, ammo=7, ammo_reach=6, ammo_attack=50)
        

class Catapult(UnitWithAmmo):
    def __init__(self):
        super().__init__("img/catapult.png", speed=0, hp=25, rest_ability=0.1, attack=74, reach=3, healing=0, ammo=5, ammo_reach=5, ammo_attack=49)