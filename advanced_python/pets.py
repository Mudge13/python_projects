class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

        else:
            return ""

    def sing(self):
        for animal in self.animals:
            voice = input(f"What sound {animal.name} makes: ")
            print(animal.sing(voice))


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'Simon is saying {sounds}'

    def walk(self):
        return f'{self.name} is running'


class Sally(Cat):
    def sing(self, sounds):
        return f'Sally is singing {sounds}'

# 1 Add nother Cat


class Tammy(Cat):
    def sing(self, sounds):
        return f'Tammy is screaming {sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = []
cat1 = Simon("simon", 19)
cat2 = Sally("sally", 22)
cat3 = Tammy("tammy", 18)
new_cats = [cat1, cat2, cat3]
my_cats.extend(new_cats)

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()
my_pets.sing()
