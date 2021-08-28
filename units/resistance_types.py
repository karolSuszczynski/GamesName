from units.attack_and_defence import AttackType, Resistance

human_resistance = Resistance()

grean_dragon_resistance = Resistance(
    {
        AttackType.BLUNT:0,
        AttackType.PIERCE:0.2,
        AttackType.SLASH:0.3,
        AttackType.HEAT:0.3,
        AttackType.COLD:-0.5,
        AttackType.POISON:0.7,
        AttackType.MAGIC:0.5,
        AttackType.ELECTRIC:0,
    }
)