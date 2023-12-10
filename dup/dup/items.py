# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LjItem(scrapy.Item):
    title = scrapy.Field()
    aid = scrapy.Field()
    price = scrapy.Field()
    unitprice = scrapy.Field()
    xiaoqu = scrapy.Field()
    jushi = scrapy.Field()
    mianji = scrapy.Field()
    chaoxiang = scrapy.Field()
    #zhuangxiu = scrapy.Field()
    louceng = scrapy.Field()
    niandai = scrapy.Field()
    #quyu = scrapy.Field()
    nianxian = scrapy.Field()
    chanquan = scrapy.Field()
    dianti = scrapy.Field()
    quanshu = scrapy.Field()
    url = scrapy.Field()

    def print1(self):
        print (self["title"])
        print (self["xiaoqu"])
        print (self["aid"])
