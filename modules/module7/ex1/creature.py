from ex0.creature import Creature
from .capability import TransformCapability, HealCapability


class Sproutling(Creature, HealCapability):

    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"

class Bloomelle(Creature, HealCapability):

    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"

class Shiftling(Creature, TransformCapability):

    def __init__(self):
        super().__init__("Shiftling", "Normal")
        self.state = False

    def attack(self) -> str:
        if self.state:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        self.state = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.state = False
        return "Shiftling returns to normal."

class Morphagon(Creature, TransformCapability):

    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")
        self.state = False

    def attack(self) -> str:
        if self.state:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self) -> str:
        self.state = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.state = False
        return "Morphagon stabilizes its form."
