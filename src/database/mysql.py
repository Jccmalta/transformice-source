import pymysql
from utils.files import *

class Mysql:
	def __init__(self, server):
		self.server = server
		# config
		self.config = eval(files.read("./files/database.json"))
		# none
		self.mysql = None
		# Connect
		self.connect()

	def connect(self):
		self.mysql = pymysql.connect(host=self.config["host"], user=self.config["user"], password=self.config["pass"], db=self.config["db"], charset=self.config["charset"], cursorclass=pymysql.cursors.DictCursor)

	def execute(self, sql="", args=tuple):
		if len(args) > 0:
			self.mysql.execute(sql, args)
		else:
			self.mysql.execute(sql)

	def close(self):
		self.mysql.close()
		self.mysql = None

	def commit(self):
		self.mysql.commit()