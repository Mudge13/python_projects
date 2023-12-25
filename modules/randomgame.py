from random import randint
from sys import argv

start_num = argv[1]
last_num = argv[2]

random_num = randint(int(start_num), int(last_num))
print(random_num)
while True:
    try:
        guess_num = int(input("guess the number: "))

        if guess_num == random_num:
            print("wow you are a genius")
            break

        elif guess_num > 10:
            print(f"Dumbass, the number is between {start_num} and {last_num}")

        else:
            print("Nope, try again")

    except:
        print("please write a valid number")
