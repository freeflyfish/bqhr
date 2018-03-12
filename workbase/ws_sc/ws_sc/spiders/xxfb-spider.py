# coding:utf-8

import scrapy


class XXFBSpider(scrapy.Spider):
    name = 'xxfb'
    start_urls = [
        'http://xxfb.hydroinfo.gov.cn/',
    ]
    allowed_domains = 'xxfb.hydroinfo.gov.cn/'