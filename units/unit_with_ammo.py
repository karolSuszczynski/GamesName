from units.base_unit import BaseUnit, get_distance
from units.attack_and_defence import calculate_damage

class UnitWithAmmo(BaseUnit):
    def __init__(self,image_path, speed, hp, rest_ability, attack, reach, healing, ammo, ammo_reach, ammo_attack):
            super().__init__(image_path, speed, hp, rest_ability, attack, reach, healing)
            self.ammo = ammo
            self.ammo_reach = ammo_reach
            self.ammo_attack = ammo_attack
            
    def get_params(self):
        params = super().get_params()
        params["ammo"] = self.ammo
        params["ammo_reach"] = self.ammo_reach
        params["ammo_attack"] = self.ammo_attack
        return params
        
    def get_action_map(self):
        if self.ammo <= 0:
            return super().get_action_map()
        action_map = self.move_action_map.get_action_map(self.speed, self.x, self.y)
        for y in range(self.battlefield.H):
            for x in range(self.battlefield.W):
                unit = self.battlefield.grid[y][x]
                if unit is not None:
                    if get_distance(self.x, self.y, x, y) <= self.ammo_reach:
                        if unit.owner != self.owner:
                            action_map[y][x] = "attack"
                        else:
                            action_map[y][x] = "support"
                    
         
        return action_map
            
    def try_attack_position(self,x,y,special):
        if self.ammo > 0 and special:
            if get_distance(self.x, self.y, x, y) > self.ammo_reach:
                return False
            target = self.battlefield.grid[y][x]
            assert target is not None
            damage = calculate_damage(self.ammo_attack, target.armor, target.resistance)
            target.get_damaged(damage)
            self.ammo -= 1
            return True
        return super().try_attack_position(x,y,special)
          