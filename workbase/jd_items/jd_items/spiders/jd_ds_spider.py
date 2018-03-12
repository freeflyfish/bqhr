# -*- coding:utf-8 -*-

import scrapy
from scrapy.http import Request, FormRequest


class JDDSSPider(scrapy.Spider):
    name = 'jd_ds'
    allowed_domains = ["https://search.jd.com"]
    start_urls = [
        'https://search.jd.com/Search?keyword=电视&enc=utf-8&wq=电视&pvid=005c31ac7e654ff2a6cd54808113ac9d'
    ]
    headers = {
        'Referer': 'https://jiadian.jd.com/',
        'User-Agent': 'Mozilla / 5.0(WindowsNT6.1;Win64;x64)AppleWebKit/537.36'
                      '(KHTML,likeGecko)Chrome/60.0.3112.113Safari/537.36'
    }

    def start_requests(self):
        yield Request(url=self.start_urls[0], headers=self.headers, callback=self.parse, dont_filter=True)

    def parse(self, response):
        lis = response.xpath('//li[@class="gl-item"]/div[@class="gl-i-wrap"]')
        for l in lis:
            yield {'remark': l.xpath('div[1]/a/@title').extract_first(),
                   'price': l.xpath('div[2]/strong/i/text()').extract_first(),
                   'title': l.xpath('div[3]/a/em/text()').extract_first(),
                   'color': l.xpath('div[3]/a/em/text()').extract()[1]
                   }
