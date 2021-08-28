from enum import Enum


class AttackType(Enum):
    BLUNT=0
    PIERCE=1,
    SLASH=2,
    HEAT=3
    COLD=4
    POISON=5
    MAGIC=6
    ELECTRIC=7

class SingleParams:
    def __init__(self, value, type=AttackType.BLUNT):
        self.value = value
        self.type = type

class Attack:
    def __init__(self, single_attacks:list):
        self.single_attacks = single_attacks

class Armor:
    def __init__(self, defence_map={}):
        self.defence_map = defence_map

    def get_value(self, type:AttackType):
        return self.defence_map.get(type, 0)

class Resistance:
    def __init__(self, resistance_map={}):
        self.resistance_map = resistance_map

    def get_value(self, type:AttackType):
        return self.resistance_map.get(type, 0)

def calculate_damage(attacks, armor, resistance):
    total_damage = 0
    for single_attacks in attacks.single_attacks:
        damage = single_attacks.value - armor.get_value(single_attacks.type)
        damage *= (1 - resistance.get_value(single_attacks.type))
        total_damage += damage
    return total_damage