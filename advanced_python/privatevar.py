class Player:
    def __init__(self, name):
        self._name = name


player1 = Player("Mihir")
print(player1._name)

player1.name = "Vridhi"
print(player1.name)
print(player1._name)
