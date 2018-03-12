# coding:utf-8

import scrapy
from scrapy.http import Request, FormRequest


class LaGoSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ["lagou.com"]
    start_urls = ['https://www.lagou.com/']
    headers = {
        'Referer': 'https://www.lagou.com/',
        'Upgrade - Insecure - Requests': '1',
        'User - Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/63.0.3239.132 Safari/537.36'
    }

    def __init__(self, **kwargs):
        super().__init__(self.name, **kwargs)

    def start_requests(self):
        yield Request(url=self.start_urls[0],
                      headers=self.headers,
                      callback=self.parse,
                      dont_filter=True,)

    def parse(self, response):
        with open('lagou.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
            f.close()