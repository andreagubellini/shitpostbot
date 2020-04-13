import requests
import random
from bs4 import BeautifulSoup


class scraper(object):
    @staticmethod
    def scrape():
        image_list = []
        thread_list = []
        boards = ['a', 'b', 'vg', 'c', 'r9k', 'mlp', 'wsg']
        board = random.choice(boards)
        board_url = 'https://boards.4channel.org/%s' %board
        page = requests.get(board_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        reply_links = soup.select('a.replylink')
        for i in reply_links:
            if 'thread' in i['href']:
                thread_list.append('https://boards.4channel.org/%s/' % board + i['href'])
        picked_thread = random.choice(thread_list)
        thread_url = picked_thread
        thread_page = requests.get(thread_url)
        thread_soup = BeautifulSoup(thread_page.content, 'html.parser')
        a_links = thread_soup.findAll('a')
        for image in a_links:
             if image.has_attr('href'):
                if '.jpg' in image['href']:
                    src = image['href']
                    image_list.append('http:'+src)
                if '.webm' in image['href']:
                    src = image['href']
                    image_list.append('http:'+src)
                if '.gif' in image['href']:
                    src = image['href']
                    image_list.append('http:'+src)
        img_pick = random.choice(image_list)
        print('thread '+picked_thread)
        print('media '+img_pick)
        return img_pick