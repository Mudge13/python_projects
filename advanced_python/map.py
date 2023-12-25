def multiply_2(item):
    return item+"hello"


data = {"name": "Mihir", "age": "too old"}
print(list(map(multiply_2, data.values())))
