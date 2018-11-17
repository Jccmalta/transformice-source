import threading
from utils.echo import *
from utils.files import *
from src.database.mysql import *

class tfm_server:
	def __init__(self):
		# list
		self.listen = []
		self.address_ban = []
		self.users_online = []
		# dict
		self.sockets = {}
		self.connections = {}
		# int
		self.last_code = 0
		# config
		self.config = eval(files.read("./files/config.json"))
		# mysql
		self.mysql = Mysql(self)
		
	def set_temp_ban(self, address=str):
		echo.log("IP temporarily banned by connection limit: {0}.".format(address))
		threading.Timer(900, self.remove_temp_ban, args=[address]).start()
		self.address_ban.append(address)

	def remove_temp_ban(self, address=str):
		self.address.remove(address)