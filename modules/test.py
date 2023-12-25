import pyjokes
from collections import Counter, defaultdict, OrderedDict
import time

# print(pyjokes.get_joke(language='en', category="all"))

# my_dict = defaultdict(lambda: "hello world", {'a': 1, 'b': 2})
# print(my_dict['c'])

my_dict = {}

my_dict['c'] = 3
my_dict['b'] = 2
my_dict['a'] = 1
print(my_dict)

my_dict2 = {'a': 1, 'b': 2, 'c': 3}
print(my_dict2)
print(my_dict == my_dict2)
