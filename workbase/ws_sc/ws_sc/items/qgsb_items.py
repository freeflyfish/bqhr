# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QgsbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()  # 城市
    city_url = scrapy.Field()  # 城市地址
    sb_url = scrapy.Field()  # 公积金地址



