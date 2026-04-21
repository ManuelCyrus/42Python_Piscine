from ex0.creatureFactory import FlameFactory, AquaFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory

from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyException
)


def battle(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    print("* Battle *")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):

            factory_a, strategy_a = opponents[i]
            factory_b, strategy_b = opponents[j]

            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()

            print(f"{creature_a.name} is a {creature_a.type} type Creature")
            print("vs.")
            print(f"{creature_b.name} is a {creature_b.type} type Creature")
            print("now fight!")

            try:
                if not strategy_a.is_valid(creature_a):
                    raise InvalidStrategyException(
                        f"Invalid Creature '{creature_a.name}' for this strategy"
                    )
                if not strategy_b.is_valid(creature_b):
                    raise InvalidStrategyException(
                        f"Invalid Creature '{creature_b.name}' for this strategy"
                    )

                print(strategy_a.act(creature_a))
                print(strategy_b.act(creature_b))

            except InvalidStrategyException as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":

    print("Tournament 0 (basic)")
    opponents0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    battle(opponents0)

    print("\nTournament 1 (error)")
    opponents1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    battle(opponents1)

    print("\nTournament 2 (multiple)")
    opponents2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]
    battle(opponents2)
