# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WsScItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    card_num = scrapy.Field()  # 卡号
    new_balance = scrapy.Field()  # 应还金额
    min_payment = scrapy.Field()  # 最小还款金额
    price_detail = scrapy.Field()  # 消费详情列表


class WsScItemDetail(scrapy.Item):
    id = scrapy.Field()   # 站口号
    t_date = scrapy.Field()  # 结束日期
    p_date = scrapy.Field()  # 起始日期
    description = scrapy.Field()  # 消费详情
    curr_price = scrapy.Field()   # 消费金额


class DKMItem(scrapy.Item):
    name = scrapy.Field()
    price_ram = scrapy.Field()
    jd_date = scrapy.Field()
    jk_type = scrapy.Field()
    xlly = scrapy.Field()
    pub_date = scrapy.Field()
    url = scrapy.Field()
    detail =scrapy.Field()
