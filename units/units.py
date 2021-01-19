from PIL import Image, ImageTk
from units.base_unit import BaseUnit
from units.unit_with_ammo import UnitWithAmmo


class Footman(BaseUnit):
    def __init__(self):
        super().__init__("img/footman.png", speed=1, hp=175, rest_ability=4, attack=10, reach=1)
        
class Axeman(BaseUnit):
    def __init__(self):
        super().__init__("img/axeman.png", speed=1, hp=100, rest_ability=4, attack=20, reach=1)
        
class Spearman(BaseUnit):
    def __init__(self):
        super().__init__("img/spearman.png", speed=1, hp=100, rest_ability=4, attack=10, reach=2)

class Horseman(BaseUnit):
    def __init__(self):
        super().__init__("img/horseman.png", speed=2, hp=100, rest_ability=4, attack=10, reach=1)
        
class Charlatan(BaseUnit):
    def __init__(self):
        super().__init__("img/charlatan.png", speed=1, hp=70, rest_ability=5, attack=2, reach=1, healing=5)   

class Infantryman(BaseUnit):
    def __init__(self):
        super().__init__("img/infantryman.png", speed=1, hp=250, rest_ability=6, attack=10, reach=1)   
     
class Bardicheman(BaseUnit):
    def __init__(self):
        super().__init__("img/bardicheman.png", speed=1, hp=100, rest_ability=6, attack=30, reach=1) 
  
class Pikeman(BaseUnit):
    def __init__(self):
        super().__init__("img/pikeman.png", speed=1, hp=100, rest_ability=6, attack=10, reach=3)   

class Cavalryman(BaseUnit):
    def __init__(self):
        super().__init__("img/cavalryman.png", speed=3, hp=100, rest_ability=6, attack=10, reach=1)   
        
class Healer(BaseUnit):
    def __init__(self):
        super().__init__("img/healer.png", speed=1, hp=100, rest_ability=10, attack=5, reach=2, healing=10) 

class Legionist(BaseUnit):
    def __init__(self):
        super().__init__("img/legionist.png", speed=1, hp=300, rest_ability=8, attack=15, reach=1)  

class Halbeldier(BaseUnit):
    def __init__(self):
        super().__init__("img/halbeldier.png", speed=1, hp=175, rest_ability=8, attack=28, reach=2)  

class Hoplite(BaseUnit):
    def __init__(self):
        super().__init__("img/hoplite.png", speed=1, hp=200, rest_ability=8, attack=15, reach=2)   

class Cataphract(BaseUnit):
    def __init__(self):
        super().__init__("img/cataphract.png", speed=3, hp=175, rest_ability=8, attack=15, reach=1) 



      



class Peasant(UnitWithAmmo):
    def __init__(self):
        super().__init__("img/peasant.png", speed=1, hp=77, rest_ability=4, attack=10, reach=1, healing=0, ammo=1, ammo_reach=4, ammo_attack=299) 
        
    def try_attack_position(self,x,y,special):
        result = super().try_attack_position(x,y,special)
        if self.ammo == 0:
            self.attack=8
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
        super().__init__("img/catapult.png", speed=0, hp=25, rest_ability=0, attack=74, reach=3, healing=0, ammo=5, ammo_reach=5, ammo_attack=49)
        
class Tower(UnitWithAmmo):
    def __init__(self):
        super().__init__("img/tower.png", speed=0, hp=999, rest_ability=0.75, attack=99, reach=1, healing=3, ammo=7, ammo_reach=5, ammo_attack=74)

