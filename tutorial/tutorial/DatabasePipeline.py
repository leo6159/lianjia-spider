from scrapy.exceptions import DropItem
import sqlite3
import time

class DatabasePipeline(object):
	def process_item(self, item, spider):
		localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		self.conn = sqlite3.connect('../../lj.db')
		self.cursor = self.conn.cursor()
		self.cursor.execute('insert into detail ' \
			+ '(title, aid, price, unitprice, xiaoqu, jushi, ' \
			+ 'mianji, chaoxiang, louceng, niandai, nianxian, ' \
			+ 'chanquan, dianti, quanshu, url, ctime, guapaidate, shangcidate, quyu,status,qu) ' \
			+ 'values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', \
			  (item["title"], item["aid"], item["price"], item["unitprice"], item["xiaoqu"], item["jushi"],\
			item["mianji"], item["chaoxiang"], item["louceng"], item["niandai"], item["nianxian"],\
			item["chanquan"], item["dianti"], item["quanshu"], item["url"], localtime, item["guapaidate"], item["shangcidate"], item["quyu"], item["status"], item["qu"]))
		self.conn.commit()
		self.conn.close()