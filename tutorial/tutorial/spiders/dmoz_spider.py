#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
抓取lj.com房源信息，本程序仅供学习交流请勿用于非法用途
'''
import scrapy
import sqlite3
from ..items import LjItem
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

class DmozSpider(scrapy.spiders.Spider):
    name = "lj"
    low_price = '100'
    high_price = '1000'

    voidValue = '无数据'
    allowed_domains = ["lianjia.com"]
    url_set = set()
    total_num = 0
    start_urls = [
        #"https://bj.lianjia.com/ershoufang/haidian/ng1hu1nb1sf1l1l2bp100ep1000/",
    
    ]
    def __init__(self):
        print( '*** init start ***')
        DmozSpider.start_urls = DmozSpider.set_start_urls()
        
        self.conn = sqlite3.connect('../../lj.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("select url,status from detail")
        capted_url_status = self.cursor.fetchall()
        self.conn.close()
        #print capted_url_status
        
        for t_url,status in capted_url_status:
            self.url_set.add(t_url)
            # print t_url + " has been capted"

        print(  '*** init end *** ')

    @staticmethod
    def set_start_urls():
        t_urls = []
        haidian = "https://bj.lianjia.com/ershoufang/co32l3l4a3a4p5p6"+"bp"+DmozSpider.low_price+"ep"+DmozSpider.high_price
        t_urls.append(haidian+"/")
        for i in range(2,9):
            t_urls.append(haidian+"pg%s"%i+"/")
        return t_urls

    def parse(self, response):
        houseNodes = response.xpath("//ul[@class='sellListContent']//div[@class='title']/a")
        for node in houseNodes:
            div_title = node.xpath("./text()").extract()[0]
            ## 取当前节点的herf属性
            a_url = node.xpath("./@href").extract()[0]
            if a_url.find("is_sem=1") != -1:
                # print "%"+a_url+' is sem'
                a_url = a_url.split('?')[0]
            if a_url in DmozSpider.url_set:
                # print '#'+a_url+' is in the set'
                pass
            else:
                DmozSpider.url_set.add(a_url)
                print ('start to catch ' + a_url)
                yield scrapy.Request(a_url, self.detail)
                
    def detail(self, response):
        title = response.xpath("/html/body/div[3]/div/div/div[1]/h1/text()").extract()[0]
        aid = response.url.split("/")[-1].split(".")[0]
        price = response.xpath("/html/body/div[5]/div[2]/div[3]/div/span[1]/text()").extract()[0]
        unitprice = response.xpath("/html/body/div[5]/div[2]/div[3]/div/div[1]/div[1]/span/text()").extract()[0]
        xiaoqu = response.xpath("/html/body/div[5]/div[2]/div[5]/div[1]/a[1]/text()").extract()[0]
        jushi = response.xpath("/html/body/div[5]/div[2]/div[4]/div[1]/div[1]/text()").extract()[0]
        mianji = response.xpath("/html/body/div[5]/div[2]/div[4]/div[3]/div[1]/text()").extract()[0]
        chaoxiang = response.xpath("/html/body/div[5]/div[2]/div[4]/div[2]/div[1]/text()").extract()[0]
        louceng = response.xpath("/html/body/div[5]/div[2]/div[4]/div[1]/div[2]/text()").extract()[0]
        niandai = response.xpath("/html/body/div[5]/div[2]/div[4]/div[3]/div[2]/text()").extract()[0]
        nianxian = response.xpath("//*[@id='introduction']/div/div/div[2]/div[2]/ul/li[5]/span[2]/text()").extract()[0]
        chanquan = response.xpath("//*[@id='introduction']/div/div/div[2]/div[2]/ul/li[6]/span[2]/text()").extract()[0]
        dianti = response.xpath("//*[@id='introduction']/div/div/div[1]/div[2]/ul/li[12]/text()").extract_first()
        quanshu = response.xpath("//*[@id='introduction']/div/div/div[2]/div[2]/ul/li[2]/span[2]/text()").extract()[0]

        guapaidate = response.xpath("//*[@id='introduction']/div/div/div[2]/div[2]/ul/li[1]/span[2]/text()").extract()[0]
        shangcidate = response.xpath("//*[@id='introduction']/div/div/div[2]/div[2]/ul/li[3]/span[2]/text()").extract()[0]
        quyu = response.xpath("/html/body/div[5]/div[2]/div[5]/div[2]/span[2]/a[2]/text()").extract()[0]
        qu = response.xpath("/html/body/div[4]/div/div/a[3]/text()").extract()[0]
        qu = qu.replace("二手房","")
        jingshoufu = response.xpath("//*[@id='calculator']/div[2]/div[1]/div[2]/div[1]/ul/li[1]/div[2]/text()").extract()
        if jingshoufu:
            jingshoufu = jingshoufu[0]
            print ("jingshoufu = "+jingshoufu)

        quyulist = ["西山"]
        url = response.url

        item = LjItem()
        item["url"] = url
        item["title"] = title
        item["aid"] = aid
        item['price'] = price
        item['unitprice'] = unitprice
        item["xiaoqu"] = xiaoqu
        item["jushi"] = jushi
        item["mianji"] = mianji
        item["chaoxiang"] = chaoxiang
        item["louceng"] = louceng
        item["niandai"] = niandai
        item["nianxian"] = nianxian
        item["chanquan"] = chanquan
        item["dianti"] = dianti
        item["quanshu"] = quanshu

        item["guapaidate"] = guapaidate
        item["shangcidate"] = shangcidate
        item["quyu"] = quyu
        item["qu"] = qu

        f_mianji = 0
        try:
            f_mianji = float(mianji.replace("平米",""))
            if quyu in quyulist or f_mianji < 50 or louceng.find("地下室") != -1:
                item["status"] = 2
            else:
                item["status"] = 0
        except ValueError:
            print("171 + ValueError"+mianji+","+url)
            pass
        else:
            print("ValueError"+mianji+","+url)
        return item
