# lianjia-spider
lianjia-spider
# 使用scrapy进行lianjia网站的信息抓取、比对和处理
## 环境
操作系统：debian 11.7

软件：python 3.9.2, pip3, scrapy 2.9

1. 安装python3.9和scrapy (https://www.ngui.cc/el/3159196.html?action=onClick)
   1. python3.9已经集成，用 python3 --version 查看，结果为3.9.2
   2. pip3 
      1. sudo apt install python3-venv python3-pip
   3. scrapy 
      1. sudo apt-get update
      2. sudo apt-get install build-essential python3-dev libssl-dev libffi-dev libxml2 libxml2-dev libxsltl-dev zliblg-dev
      3. sudo pip3 install Scrapy
   4. scrapy version查看，Scrapy 2.9.0