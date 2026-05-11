import time
from functools import wraps
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    """
    Measure spell execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Casting {func.__name__}...")

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        execution_time = end_time - start_time

        print(
            f"Spell completed in "
            f"{execution_time:.3f} seconds"
        )

        return result

    return wrapper


def power_validator(
    min_power: int
) -> Callable:
    """
    Validate spell power before casting.
    """

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):

            power = args[-1]

            if power < min_power:
                return (
                    "Insufficient power "
                    "for this spell"
                )

            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(
    max_attempts: int
) -> Callable:
    """
    Retry failed spells.
    """

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(
                1,
                max_attempts + 1
            ):

                try:
                    return func(*args, **kwargs)

                except Exception:

                    if attempt < max_attempts:

                        print(
                            "Spell failed, retrying... "
                            f"(attempt "
                            f"{attempt}/"
                            f"{max_attempts})"
                        )

            return (
                "Spell casting failed after "
                f"{max_attempts} attempts"
            )

        return wrapper

    return decorator


class MageGuild:
    """
    Mage guild management system.
    """

    @staticmethod
    def validate_mage_name(
        name: str
    ) -> bool:
        """
        Validate mage names.
        """

        cleaned_name = name.replace(" ", "")

        return (
            len(name) >= 3
            and cleaned_name.isalpha()
        )

    @power_validator(10)
    def cast_spell(
        self,
        spell_name: str,
        power: int
    ) -> str:
        """
        Cast a guild spell.
        """

        return (
            f"Successfully cast "
            f"{spell_name} "
            f"with {power} power"
        )


# -------------------------
# Example functions
# -------------------------

@spell_timer
def fireball() -> str:

    time.sleep(0.1)

    return "Fireball cast!"


@retry_spell(3)
def unstable_spell() -> str:

    raise RuntimeError(
        "Spell instability"
    )


# -------------------------
# Tests
# -------------------------

if __name__ == "__main__":

    print("Testing spell timer...")

    result = fireball()

    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    print(unstable_spell())

    print("\nTesting MageGuild...")

    print(
        MageGuild.validate_mage_name(
            "Merlin"
        )
    )

    print(
        MageGuild.validate_mage_name(
            "X1"
        )
    )

    guild = MageGuild()

    print(
        guild.cast_spell(
            "Lightning",
            15
        )
    )

    print(
        guild.cast_spell(
            "Spark",
            5
        )
    )