# -*- coding:utf-8 -*-

import scrapy
from scrapy.http import Request, FormRequest
import time

from scrapy.spidermiddlewares.httperror import HttpError
from twisted.web._newclient import ResponseNeverReceived, ConnectionAborted


class JDDSSPider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ["https://search.jd.com"]
    start_urls = [
        'http://127.0.0.1:8000/hello/'
    ]
    headers = {
        'Referer': 'https://jiadian.jd.com/',
        'User-Agent': 'Mozilla / 5.0(WindowsNT6.1;Win64;x64)AppleWebKit/537.36'
                      '(KHTML,likeGecko)Chrome/60.0.3112.113Safari/537.36'
    }
    count = 0

    def start_requests(self):
        self.count += 1
        yield Request(url=self.start_urls[0], headers=self.headers, callback=self.parse, dont_filter=True,
                      errback=self.err_callback)
        print(self.count)

    def err_callback(self, failure):
        if failure.check(HttpError) and failure.value.response.status == 500:
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            return  # 有时会出现500错误，所以忽略

        self.logger.warning(repr(failure))
        if hasattr(failure, "type") and failure.type is ResponseNeverReceived:  # 被封锁了
            self.logger.critical("连接被重置")
            time.sleep(60 * 10)

        if '10061' in str(failure.value):
            self.logger.critical("访问连接被拒绝")
            print('停止5秒')
            for x in range(5):
                print(x)
                time.sleep(1)
        try:
            return failure.request
        except Exception:
            self.logger.exception("err_callback except")
            return [Request(url='https://www.baidu.com', callback=self.parse, dont_filter=True,
                          errback=self.err_callback)]

    def parse(self, response):
        print(response.url)
        print(response.text)