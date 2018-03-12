# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DKMItem(scrapy.Item):
    name = scrapy.Field()
    price_ram = scrapy.Field()
    jd_date = scrapy.Field()
    jk_type = scrapy.Field()
    xlly = scrapy.Field()
    pub_date = scrapy.Field()
    url = scrapy.Field()
    detail =scrapy.Field()
