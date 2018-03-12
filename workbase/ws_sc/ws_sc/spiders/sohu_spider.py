# coding:utf-8

import hashlib
import time
import scrapy
from scrapy.http import Request,FormRequest

from json import loads


class EmailSohuSpider(scrapy.Spider):
    name = 'sohu'
    allowed_domains = 'sohu.com'
    custom_settings = {
        'DOWNLOAD_DELAY': 1,  # 防封杀
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
    }
    start_urls = [
        'https://mail.sohu.com/fe/#/login',
    ]

    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Referer': 'https://mail.sohu.com/fe/',
        'User-Agent': 'Mozilla / 5.0(WindowsNT6.1;Win64;x64) AppleWebKit/537.36(KHTML,likeGecko) Chrome/60.0.3112.113Safari/537.36'
    }

    count_n = 0  # 计数

    def start_requests(self):
        yield Request(url=self.start_urls[0], callback=self.parse, dont_filter=True, meta={'cookiejar':1})

    def parse(self, response):
        username = 'xiongtaozt@sohu.com'
        password = 'scx1123'
        url_login = 'https://mail.sohu.com/fe/anoy/login'
        md5 = hashlib.md5(password.encode('utf-8'))
        data = '{"username":"%s","password":"%s","m":1,"autologin":false}' % (username, md5.hexdigest())
        print(data)

        yield FormRequest(url=url_login, body=data.encode('utf-8'), headers=self.headers,
                          meta={"cookiejar": response.meta['cookiejar']},
                          callback=self.parse_detail, method='POST', dont_filter=True)

    def parse_detail(self, response):
        print(response.headers)

        # 获取邮件内容请求
        url_detail = 'https://mail.sohu.com/fe/getList?offset=%s&limit=20&folderId=1&order=id&sort=0&t=%s' % (0, str(int(time.time() * 1000)))
        print(response.text)
        try:
            result = loads(response.text)
            if result['msg'] == 'Success':
                yield Request(url=url_detail, callback=self.parse_lis, headers=self.headers,
                              meta={"cookiejar": response.meta['cookiejar']}, dont_filter=True)

        except Exception as e:
            pass

    def parse_lis(self, response):
        # 得到详情页面html
        # url = 'https://mail.sohu.com/fe/getMail?id=3&t=1505960030173'
        print(response.text)
        print(response.meta['cookiejar'])
        lis = loads(response.text)
