# coding:utf-8

import pymongo


class PipelineUtil(object):

    def __init__(self, host, port, spider_name):
        # 数据库连接
        self.client = pymongo.MongoClient(host=host, port=port)
        self.db = self.client[spider_name]
        self.coll = self.db[spider_name]

    def process_item(self, item, spider):
        postitem = dict(item)
        self.coll.insert(postitem)
        return item
