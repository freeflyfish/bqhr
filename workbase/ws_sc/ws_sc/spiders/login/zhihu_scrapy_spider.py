# coding:utf-8

import scrapy
from scrapy.http import Request,FormRequest



class zhiHuSpider(scrapy.Spider):

    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/signup?next=%2F', ]
