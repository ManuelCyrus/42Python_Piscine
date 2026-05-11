from functools import (
    lru_cache,
    partial,
    reduce,
    singledispatch
)
from operator import add, mul
from collections.abc import Callable
from typing import Any


def spell_reducer(
    spells: list[int],
    operation: str
) -> int:
    """
    Reduce spell powers using functools.reduce.
    """

    if not spells:
        return 0

    operations = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise ValueError(
            f"Unknown operation: {operation}"
        )

    return reduce(
        operations[operation],
        spells
    )


def partial_enchanter(
    base_enchantment: Callable
) -> dict[str, Callable]:
    """
    Create specialized enchantments using partial.
    """

    return {
        "fire": partial(
            base_enchantment,
            50,
            "Fire"
        ),
        "ice": partial(
            base_enchantment,
            50,
            "Ice"
        ),
        "shadow": partial(
            base_enchantment,
            50,
            "Shadow"
        )
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    Cached fibonacci implementation.
    """

    if n < 0:
        raise ValueError(
            "Fibonacci requires n >= 0"
        )

    if n in (0, 1):
        return n

    return (
        memoized_fibonacci(n - 1)
        + memoized_fibonacci(n - 2)
    )


def spell_dispatcher() -> Callable[[Any], str]:
    """
    Create a single dispatch spell system.
    """

    @singledispatch
    def cast_spell(spell: Any) -> str:
        return "Unknown spell type"

    @cast_spell.register
    def _(spell: int) -> str:
        return (
            f"Damage spell: "
            f"{spell} damage"
        )

    @cast_spell.register
    def _(spell: str) -> str:
        return (
            f"Enchantment: "
            f"{spell}"
        )

    @cast_spell.register
    def _(spell: list) -> str:
        return (
            f"Multi-cast: "
            f"{len(spell)} spells"
        )

    return cast_spell


# -------------------------
# Example enchantment
# -------------------------

def enchantment(
    power: int,
    element: str,
    target: str
) -> str:
    return (
        f"{element} enchantment "
        f"with {power} power on {target}"
    )


# -------------------------
# Tests
# -------------------------

if __name__ == "__main__":

    print("Testing spell reducer...")

    values = [10, 20, 30, 40]

    print(f"Sum: {spell_reducer(values, 'add')}")
    print(
        f"Product: "
        f"{spell_reducer(values, 'multiply')}"
    )
    print(f"Max: {spell_reducer(values, 'max')}")
    print(f"Min: {spell_reducer(values, 'min')}")

    print("\nTesting partial enchanter...")

    enchantments = partial_enchanter(
        enchantment
    )

    print(enchantments["fire"]("Sword"))
    print(enchantments["ice"]("Shield"))
    print(enchantments["shadow"]("Dagger"))

    print("\nTesting memoized fibonacci...")

    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nCache info:")
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")

    dispatcher = spell_dispatcher()

    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.14))