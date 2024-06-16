# lianjia-spider
# 使用scrapy进行lianjia网站的信息抓取、比对和处理
## 环境
操作系统：debian 11.7

软件：python 3.9.2, pip3, scrapy 2.9

数据库：sqlite3

1. 安装python3.9和scrapy
   1. python3.9已经集成，用 python3 --version 查看，结果为3.9.2
   2. pip3 
      1. sudo apt install python3-venv python3-pip
   3. scrapy 
      1. sudo apt-get update
      2. sudo apt-get install build-essential python3-dev libssl-dev libffi-dev libxml2 libxml2-dev libxsltl-dev zliblg-dev
      3. sudo pip3 install Scrapy
   4. scrapy version查看，Scrapy 2.9.0
2. 将程序下载解压到debian中
3. 修改run-tutorial.sh的权限
   1. chmod 755 run-tutorial.sh
4. 执行./run-tutorial.sh，默认会采集北京市海淀区100-1000个w的房源信息并入库，存入lj.db。其中lj.db是sqlite3数据库，只有一个主表。

### windows下的环境搭建
使用anaconda环境

## 使用说明
1. 主要程序逻辑与参数位置：tutorial/tutorial/spiders/dmoz_spider.py
   1. low_price： 准备采集的最低房价
   2. high_price： 准备采集的最高房价
   3. set_start_urls 采集url链接集合
   4. capted_url_status 已采集链接，避免重复采集入库

## 更新记录
2024-6-16 链家更新了反爬机制，可以看到有code 418 的错误，这需要讲request中的header设置一下。
方法有几种，简单的可以在settings.py 中打开DEFAULT_REQUEST_HEADERS的注释，并写入相应的请求头信息，如：
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}
