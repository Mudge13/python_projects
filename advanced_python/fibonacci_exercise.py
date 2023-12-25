def fib_generator(place):
    a = 0
    b = 1

    for i in range(place):
        yield a
        temp = a
        a = b
        b += temp


for i in fib_generator(10):
    print(i)

print(list(fib_generator(10)))
