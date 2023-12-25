import requests
from bs4 import BeautifulSoup
import pprint

mega_links = []
mega_subtext = []
for i in range(1, 3):
    res = requests.get(f'https://news.ycombinator.com/?p={i}')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titleline > a')
    subtext = soup.select('.subtext')
    mega_links = mega_links + links
    mega_subtext = mega_subtext + subtext


def sorted_hn(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)


def custom_hn(links, subtext):
    hn = []

    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        votes = subtext[index].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(" points", ''))

            if points > 99:

                hn.append({'title': title, 'link': href, 'votes': points})
    return sorted_hn(hn)


a = custom_hn(mega_links, mega_subtext)
pprint.pprint(a)
