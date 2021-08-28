from units.attack_and_defence import AttackType, Attack, SingleParams

def get_sword_attack(level = 10):
    return Attack([
        SingleParams(0.2 * level, AttackType.BLUNT),
        SingleParams(0.5 * level, AttackType.PIERCE),
        SingleParams(level, AttackType.SLASH)
    ])

def get_claw_dragon_attack(level = 100):
    return Attack([
        SingleParams(0.5 * level, AttackType.BLUNT),
        SingleParams(0.5 * level, AttackType.PIERCE),
        SingleParams(0.5 * level, AttackType.SLASH),
        SingleParams(0.5 * level, AttackType.SLASH),
    ])