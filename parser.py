# -*- coding: utf-8 -*-
import urlparse
# from crawler import downloader
import re

from bs4 import BeautifulSoup

class Parser(object):

    def parse(self, cur_url, text):
        soup = BeautifulSoup(text, 'html.parser', from_encoding='utf-8')
        links = soup.find_all('a', href=re.compile(r"/wiki/\w+\_*\w*"))
        title = soup.find('h1', id='firstHeading')
        p = soup.find('p')

        new_urls = set()
        for link in links:
            if link.has_attr('href'):
                url = link['href']
                full_url = urlparse.urljoin(cur_url, url)
                new_urls.add(full_url)

        data = {}
        data['url'] = cur_url
        if title is not None:
            data['title'] = title.get_text()
        if p is not None:
            data['p'] = p.get_text()

        return new_urls, data