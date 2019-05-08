# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TuniuItem(scrapy.Item):
    # define the fields for your item here like:
    # productname = scrapy.Field()
    # productshortdesc = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 出行类型
    traveltype = scrapy.Field()
    # 出行路线
    travelway = scrapy.Field()
    # 出发地
    startplace = scrapy.Field()
    # 简介
    extrashortdesc = scrapy.Field()
    # 团期
    tuanqi = scrapy.Field()
    # 满意度
    satisfactionrate = scrapy.Field()
    # 出游人数
    chuyou = scrapy.Field()
    # 点评人数
    comment = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # pass
