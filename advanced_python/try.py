while True:
    try:
        age = int(input("enter your age: "))
        print(f"you are {age} years old")
        10/age
        break

    except ValueError:
        print("please enter a valid age")

    except:
        print("cant divide by 0")


