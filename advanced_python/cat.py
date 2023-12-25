# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Mihir", 18)
cat2 = Cat("Vridhi", 22)
cat3 = Cat("Arnav", 20)


# 2 Create a function that finds the oldest cat
cat_list = [cat1, cat2, cat3]
cat_age_list = []


def oldest_cat():
    for i in cat_list:
        cat_age_list.append(i.age)

    return (max(cat_age_list))


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"the oldest cat is {oldest_cat()} years old")
