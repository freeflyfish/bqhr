# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import os.path as os_path
from scrapy import signals
file = os_path.dirname(os_path.abspath(__file__))


with open(file + '\proxies.txt', 'r') as f:
    IPPOOL = [{'ipaddr': x[:-1]} for x in f.readlines()]
    if IPPOOL == None:
        pass


class MyproxiesSpiderMiddleware(object):
    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        thisip = random.choice(IPPOOL)
        print("this is ip:" + thisip["ipaddr"])
        request.meta["proxy"] = thisip["ipaddr"]