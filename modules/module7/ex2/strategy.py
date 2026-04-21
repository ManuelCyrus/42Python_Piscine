from abc import ABC, abstractmethod

class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature) -> str:
        pass

class NormalStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return True

    def act(self, creature) -> str:
        return creature.attack()

class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return hasattr(creature, "heal")

    def act(self, creature) -> str:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.name}' for this defensive strategy"
            )

        result = creature.attack()
        heal_result = creature.heal()
        return result + "\n" + heal_result

class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return hasattr(creature, "transform") and hasattr(creature, "revert")

    def act(self, creature) -> str:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.name}' for this aggressive strategy"
            )

        result = []
        result.append(creature.transform())
        result.append(creature.attack())
        result.append(creature.revert())

        return "\n".join(result)
