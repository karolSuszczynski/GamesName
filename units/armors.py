from units.attack_and_defence import AttackType, Armor

def get_leather_armor(quality=1):
    return Armor(
        {
            AttackType.BLUNT: 1 + 1*quality,
            AttackType.PIERCE: 3*quality,
            AttackType.SLASH: 4*quality,
            AttackType.HEAT: 2*quality,
            AttackType.COLD: 3 + 2*quality,
            AttackType.POISON: 0,
            AttackType.MAGIC: 0,
            AttackType.ELECTRIC: 1 + 2*quality,
        }
    )

def get_green_dragon_armor(quality=1):
    return Armor(
        {
            AttackType.BLUNT: 10*quality,
            AttackType.PIERCE: 20*quality,
            AttackType.SLASH: 20*quality,
            AttackType.HEAT: 10*quality,
            AttackType.COLD: 1*quality,
            AttackType.POISON: 10*quality,
            AttackType.MAGIC: 10*quality,
            AttackType.ELECTRIC: 2*quality,
        }
    )

no_clothes =  Armor()
no_armor = get_leather_armor(0)
peasent_armor = get_leather_armor(0.5)
leather_armor = get_leather_armor(1)

