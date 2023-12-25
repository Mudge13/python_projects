from random import randint
from sys import argv

# start_num = argv[1]
# last_num = argv[2]

# random_num = randint(int(start_num), int(last_num))
start_num = 1
last_num = 10
random_num = randint(start_num, last_num)
print(random_num)


def guess_fun(guess_num, random_num):
    if guess_num == random_num:
        print("wow you are a genius")
        return True

    elif guess_num > 10:
        print(f"Dumbass, the number is between {start_num} and {last_num}")

    else:
        print("Nope, try again")


if __name__ == "__main__":
    while True:
        try:
            guess_num = int(input("guess the number: "))

            if guess_fun(guess_num, random_num):
                break

        except:
            print("please write a valid number")
