class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,
        }

    def loc(self):
        return self

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __call__(self):
        return "yass?"

    def __getitem__(self, i):
        return self.my_dict[i]

    def __bytes__(self):
        return b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __format__(self, word):  # not working too complex
        return f"hello world {word}"

    def __hash__(self):
        return 100


action_figure = Toy('red', 0)
# z = action_figure
# print(z)
# print(type(z))

# x = action_figure()
# print(x)
# print(type(x))

# print(hash(action_figure))
# print(hash("hello world"))

# print(action_figure.format("baba"))   Not working too complex
# print("hello world {}".format("ooga"))

# b = action_figure.__str__()
# print(b)
# print(type(b))

# a = str(action_figure)
# print(a)
# print(type(a))

# print(len(action_figure))

# print(action_figure.loc())

# print(action_figure['name'])

# print(bytes(action_figure))
# print(bytes(20))
