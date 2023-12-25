import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body.contents)
# print(soup.find_all("a"))
print(soup.find(id="score_36842239"))
