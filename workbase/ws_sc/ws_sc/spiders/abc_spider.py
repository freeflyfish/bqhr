# -*- coding:utf-8 -*-

import time
import scrapy
from scrapy.http import Request
from selenium import webdriver


class AbcCrarlSpider(scrapy.Spider):
    name = 'bank_abc_carl'
    allowed_domains = ["abchina.com"]
    start_urls = ["http://www.abchina.com/cn/"]
    username = '18688983498'
    password = 'pm988311'
    cark = '6228480128558663877'

    def start_requests(self):
        driver = webdriver.Ie(executable_path='D:\\IEDriverServer_233.exe')
        driver.get('')

    def parse(self, response):
        pass

