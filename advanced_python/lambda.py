a = [5, 4, 3]

# b = lambda a: a*2


# print(b(a))

print(list(map(lambda item: item*item, a)))

b = [(0, 2), (4, 3), (9, 9), (10, -1)]

a = b.copy()
b.sort(key=lambda x: x[1])
print(a)
print(b)
