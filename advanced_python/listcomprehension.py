# print(list(range(100)))
# print(list(num*2 for num in range(100)))
my_list = [num**2 for num in range(100) if (num**2) < 121]
print(tuple(my_list))
