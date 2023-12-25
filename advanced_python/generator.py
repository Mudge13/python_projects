def my_generator(num):  # template to create a generator
    for i in range(num):
        yield i


a = my_generator(100)
print(a)
print(next(a))
# for item in my_generator(100):
#     print(item)
