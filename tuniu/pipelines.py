# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class TuniuPipeline(object):
    # 可选，作为类的初始化方法
    def __init__(self):
        self.filename = open("tuniu.json", "w", encoding="utf-8")

    # 必选，处理item数据
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.filename.write(str(jsontext))
        return item

    # 可选，结束时调用
    def close_spider(self, spider):
        self.filename.close()
