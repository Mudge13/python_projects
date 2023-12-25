# https://haveibeenpwned.com/Passwords
# CBFDAC6008F9CAB4083784CBD1874F76618D2A97

txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

squares_gen = (x**2 for x in range(1, 6))
print(type(squares_gen))  # Output: <class 'generator'>
for square in squares_gen:
    print(square)

a = "hello my friend how are you i am under the water"
for letter in a:
    print(letter.split(" "))
