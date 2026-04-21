from ex0 import FlameFactory, AquaFactory

flame = FlameFactory()
aqua = AquaFactory()

bd = aqua.create_base()

print(bd.describe())


