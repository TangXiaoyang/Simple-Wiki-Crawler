# -*- coding: utf-8 -*-
class UrlManager(object):

    def __init__(self):
        self.old_urls = set()
        self.new_urls = set()


    def has_url(self):
        return len(self.new_urls) > 0

    def add_url(self, url):
        if url is None:
            return
        if url not in self.old_urls and url not in self.new_urls:
            self.new_urls.add(url)

    def add_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_url(url)

    def get_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url