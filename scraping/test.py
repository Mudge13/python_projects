import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(res.text, 'html.parser')

# links = soup.select('.titleline > a')
# votes = soup.select('.subtext')
# points = votes[0].select('.score')
# print(votes[0])
# print(f'points are {points}')

# points = soup.select('.score')

# dict = {'a': 1, 'b': 3}
# sorted_dict = sorted(dict, key=lambda k: [])

a = int(('2,615').replace(",", ""))
print(a)
