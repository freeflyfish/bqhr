# -*- coding:utf-8 -*-

import time
import scrapy
from scrapy.http import Request
from selenium import webdriver


class DLDLSpider(scrapy.Spider):
    name = 'bqg'
    allowed_domains = ["biquge.com"]
    start_urls = ["http://www.biquge.info/10_10218/5001527.html"]
    # username = '18688983498'
    # password = 'pm988311'
    # cark = '6228480128558663877'
    path = 'E:\\xiaoshuo\dldl\\'

    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        content_list = response.xpath('//div[@id="content"]/text()').extract()
        page_next = response.xpath('//a/@href').extract()[37]
        con = ''
        if content_list:
            for x in content_list:
                con += x.replace('\r', '').replace('\n', '').replace('\xa0', '') + '\n'
        with open(self.path+title+'.txt', 'w') as f:
            f.write(con)
            f.close()
        if page_next:
            yield Request(page_next, callback=self.parse, dont_filter=True)