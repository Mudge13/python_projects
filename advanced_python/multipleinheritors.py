class Archer:
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def quiver(self):
        print(f"arrows left: {self.arrows}")


class Soldier:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"you attack with strength of {self.power}")


class Jack(Archer, Soldier):

    def __init__(self, name, arrows, power):
        Soldier.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


player1 = Jack("Mihir", 100, 50)
player1.quiver()
player1.attack()
