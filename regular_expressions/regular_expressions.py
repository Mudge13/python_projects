import re

string = "hello my name Mihir, my name is king Mihir"

# a = re.search("my", string)
# a1 = re.findall("my", string)
# print(a1)

# pattern = re.compile(r"(e).(M).([a-zA-Z])")
# b = pattern.search(string)
# b1 = pattern.findall(string)
# print(b.group(3))

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email = "mihir@gmail.com"
c = pattern.fullmatch(email)
print(c)
print(c.group())

if c:
    print("valid")
else:
    print("unvalid email")
