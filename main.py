# -*- coding: utf-8 -*-
from crawler import downloader, outputer, parser, url_manager


class Main(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = downloader.Downloader()
        self.parser = parser.Parser()
        self.outputer = outputer.Outputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_url(root_url)
        while self.urls.has_url():
            new_url = self.urls.get_url()
            print 'crawing No.%d: %s'%(count, new_url)
            response_text = self.downloader.download(new_url)
            other_urls, parse_data = self.parser.parse(new_url, response_text)
            self.urls.add_urls(other_urls)
            self.outputer.collect_data(parse_data)

            if count == 10:
                break
            count += 1

        self.outputer.output_html()




if __name__ == "__main__":
    root_url = "https://en.wikipedia.org/wiki/World_War_II"
    main_obj = Main()
    main_obj.craw(root_url)
