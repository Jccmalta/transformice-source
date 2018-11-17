import socket
import asyncore
import threading
from server.client import *
from utils.echo import *
from utils.files import *

class asyncore_server(asyncore.dispatcher):
	def __init__(self, server, host=str, port=int):
		# server
		self.__server = server
		# Initialize asyncore
		asyncore.dispatcher.__init__(self)
		# config file
		self.__config = eval(files.read("./files/socket.json"))
		# Dict
		self.__sockets = {}
		# Start sockets
		self.open_sockets(host, port)

	def open_sockets(self, host, port):
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.bind((host, port))
		self.listen(self.__config["listen"])
		self.__server.listen.append(port)
		threading.Thread(target=asyncore.loop).start()

	def handle_accepted(self, socket, address):
		if address[0] in self.__server.address_ban:
			self.close()
			return

		if address[0] in self.__server.connections.keys():
			self.__server.connections[address[0]] += 1
		else:
			self.__server.connections[address[0]] = 1

		if self.__server.connections[address[0]] > self.__config["ip_conn"]:
			self.__server.set_temp_ban(address[0])
			self.close()
			return
		else:
			echo.log("New client connected: {0}.".format(address[0]))
			client = tfm_client(self.__server, socket, address)