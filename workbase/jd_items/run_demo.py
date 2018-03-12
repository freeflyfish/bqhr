# -*- coding: utf-8 -*-

from os import path as os_path
from sys import path as sys_path
from multiprocessing import Process

sys_path.append(os_path.dirname(os_path.abspath(__file__)))

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from jd_items.spiders.demo_spider import JDDSSPider


def start_water_crawler():
    process = CrawlerProcess(get_project_settings())
    process.crawl(JDDSSPider)
    process.start()


def crawl_water_info(process_count=1):
    process_list = []
    for i in range(process_count):
        p = Process(target=start_water_crawler)
        process_list.append(p)
        p.start()

if __name__ == '__main__':
    crawl_water_info(process_count=1)
