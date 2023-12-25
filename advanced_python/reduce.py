from functools import reduce

my_list = [1, 2, 3]


def accumulator(mcc, item):
    print(mcc, item)
    return mcc * item


print(reduce(accumulator, my_list))
