# atleast 8 char
# contain any sort of letter, numbers, $%#@

import re

pattern = re.compile(
    r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).*$")

while True:
    password = input("enter you password: ")
    a = pattern.fullmatch(password)
    print(a.group())

    if a:
        print("valid")
        break
    else:
        print("unvalid password")
