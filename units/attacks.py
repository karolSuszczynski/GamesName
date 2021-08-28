from units.attack_and_defence import AttackType, Attack, SingleParams

def get_sword_attack(level = 10):
    result = Attack([
        SingleParams(0.2 * level, AttackType.BLUNT),
        SingleParams(0.5 * level, AttackType.PIERCE),
        SingleParams(level, AttackType.SLASH)
    ])
    return result

