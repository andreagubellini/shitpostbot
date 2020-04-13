import requests
import random
from bs4 import BeautifulSoup


class scraper(object):
    @staticmethod
    def scrape():
        boards = ['a', 'b', 'vg', 'c', 'r9k', 'mlp', 'wsg']
        board = random.choice(boards)
        url = 'https://boards.4channel.org/%s' %board
        page = requests.get(url)
        src_list = []
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.findAll('a')
        for link in links:
             if link.has_attr('href'):
                if '.jpg' in link['href']:
                    src = link['href']
                    src_list.append('http:'+src)
                if '.webm' in link['href']:
                    src = link['href']
                    src_list.append('http:'+src)
                if '.gif' in link['href']:
                    src = link['href']
                    src_list.append('http:'+src)
        img_pick = random.choice(src_list)
        print(img_pick)
        return img_pick