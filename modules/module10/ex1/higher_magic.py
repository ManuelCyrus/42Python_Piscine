from collections.abc import Callable


def spell_combiner(
    spell1: Callable,
    spell2: Callable
) -> Callable:
    """
    Combine two spells into one.
    """

    def combined(target: str, power: int) -> tuple:
        return (
            spell1(target, power),
            spell2(target, power)
        )

    return combined


def power_amplifier(
    base_spell: Callable,
    multiplier: int
) -> Callable:
    """
    Amplify spell power before casting.
    """

    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(
    condition: Callable,
    spell: Callable
) -> Callable:
    """
    Cast spell only if condition passes.
    """

    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)

        return "Spell fizzled"

    return conditional


def spell_sequence(
    spells: list[Callable]
) -> Callable:
    """
    Cast multiple spells in sequence.
    """

    def sequence(target: str, power: int) -> list[str]:
        return [
            spell(target, power)
            for spell in spells
        ]

    return sequence


# -------------------------
# Example spells
# -------------------------

def fireball(target: str, power: int) -> str:
    return (
        f"Fireball hits {target} "
        f"for {power} damage"
    )


def heal(target: str, power: int) -> str:
    return (
        f"Heal restores {target} "
        f"for {power} HP"
    )


def lightning(target: str, power: int) -> str:
    return (
        f"Lightning shocks {target} "
        f"for {power} damage"
    )


# -------------------------
# Example condition
# -------------------------

def strong_enough(
    target: str,
    power: int
) -> bool:
    return power >= 50


# -------------------------
# Tests
# -------------------------

if __name__ == "__main__":

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)

    result = combined("Dragon", 30)

    print(result)

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)

    print("Original:")
    print(fireball("Ogre", 10))

    print("Amplified:")
    print(mega_fireball("Ogre", 10))

    print("\nTesting conditional caster...")
    safe_spell = conditional_caster(
        strong_enough,
        lightning
    )

    print(safe_spell("Goblin", 20))
    print(safe_spell("Goblin", 80))

    print("\nTesting spell sequence...")
    combo = spell_sequence(
        [fireball, heal, lightning]
    )

    results = combo("Titan", 40)

    for spell_result in results:
        print(spell_result)