class NewPlayer:
    title = "captain"

    def __init__(self, name):
        self.name = name

    def run(self):
        # we need to write self.title as it doesnt execute already
        print(f"run {self.title} {self.name}")

    def loc(self):
        return self


player1 = NewPlayer("Mihir")

player1.attack = 50
print(player1.name)

title = "Kaicho"  # changes title if self.title is not written
player1.run()

print(player1.attack)

print(player1.loc())
print(player1)
a = player1.loc()
print(a.loc())
