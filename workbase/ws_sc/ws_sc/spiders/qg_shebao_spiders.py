# coding:utf-8

import scrapy
from scrapy.http import Request, FormRequest
from ws_sc.items.qgsb_items import QgsbItem


class QgShebaoSpider(scrapy.Spider):
    name = 'qgsb'
    allowed_domains = '12333sb.com'
    start_urls = ['http://www.12333sb.com/gongjijin/', ]

    def parse(self, response):

        items = response.xpath('//div[@class="neirong"]/a')
        for item in items:
            qgsb = QgsbItem()
            qgsb['city'] = item.xpath('text()').extract_first()
            qgsb['city_url'] = item.xpath('@href').extract_first()
            yield Request(url='http://www.12333sb.com/' + qgsb['city_url'], callback=self.parse_detail,
                          meta={'item': qgsb}, dont_filter=True)

    def parse_detail(self, response):
        qgsb = response.meta['item']
        try:
            qgsb['sb_url'] = response.xpath('//div[@class="gaikuang"]/a/@href').extract_first()
        except Exception as e:
            self.logger(e)
        yield qgsb
