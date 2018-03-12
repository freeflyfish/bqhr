# coding: utf-8

import scrapy
import time
import json
import requests
from urllib.parse import quote
from scrapy.http import Request, FormRequest
from ws_sc.items.dkm_items import DKMItem


class DKMSpider(scrapy.Spider):
    name = 'dkm'
    allowed_domains = ["dailianmeng.com"]
    username = '刘力'
    data = {
        'SearchForm[verifyCode]': '',
        'yt0': '',
    }
    start_urls = ['http://www.dailianmeng.com',
                  'http://www.dailianmeng.com/xinyong/captcha.html?refresh=1&_=%s' % str(int(time.time() * 1000)),
                  'http://www.dailianmeng.com/xinyong/q/%s.html' % quote(username)
                ]
    headers = {
        'Referer': start_urls[2],  # %E7%8E%8B%E6%9E%97
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }

    def start_requests(self):
        yield Request(url=self.start_urls[1], headers=self.headers, callback=self.parse, dont_filter=True)

    def parse(self, response):
        try:
            # 得到验证码请求
            json_url = json.loads(response.body)['url']
            yield Request(url=self.start_urls[0]+json_url, headers=self.headers, callback=self.parse_vcode, dont_filter=True)
        except Exception as e:
            pass

    def parse_vcode(self, response):
        # 得到验证,存储验证码
        try:
            with open('vcode.jpg', 'wb') as f:
                f.write(response.body)
            self.data['SearchForm[verifyCode]'] = input('>')
            yield FormRequest(url=self.start_urls[2], formdata=self.data, headers=self.headers,
                              callback=self.parse_detail, dont_filter=True)
        except Exception as e:
            pass

    def parse_detail(self, response):

        try:
            trs = response.xpath('//table/tbody/tr')
            for tr in trs:
                dkm = DKMItem()
                dkm['name'] = tr.xpath('td[2]/text()').extract_first() if tr.xpath('td[2]/text()') != [] else None
                dkm['price_ram'] = tr.xpath('td[3]/text()').extract_first() if tr.xpath('td[3]/text()') != [] else None
                dkm['jd_date'] = tr.xpath('td[4]/text()').extract_first() if tr.xpath('td[4]/text()') != [] else None
                dkm['jk_type'] = tr.xpath('td[5]/text()').extract_first() if tr.xpath('td[5]/text()') != [] else None
                dkm['xlly'] = tr.xpath('td[6]/text()').extract_first() if tr.xpath('td[6]/text()') != [] else None
                dkm['pub_date'] = tr.xpath('td[7]/text()').extract_first() if tr.xpath('td[7]/text()') != [] else None
                dkm['url'] = tr.xpath('td[8]/a/@href').extract_first() if tr.xpath('td[8]/a/@href') != [] else None

                yield Request(url=self.start_urls[0] + dkm['url'], headers=self.headers, meta={'dkm': dkm},
                              callback=self.parse_cont, dont_filter=True)
        except Exception as e:
            pass

    def parse_cont(self, response):
        dkm = response.meta['dkm']
        detail = dict()
        try:
            trs = response.xpath('//table/tr')
            for tr in trs:
                detail[tr.xpath('th/text()').extract_first()] = \
                    tr.xpath('td/text()').extract_first() if tr.xpath('td/text()') != [] else None
            dkm['detail'] = detail

        except Exception:
            pass
        yield dkm
