import asyncore
import threading
from utils.echo import *
from src.handler import *
from src.manager import *

class tfm_client(asyncore.dispatcher):
	def __init__(self, server, socket, address):
		asyncore.dispatcher.__init__(self, socket)
		# socket
		self.server = server
		self.socket = socket
		self.address = address
		# int
		self.packet_id = 0
		self.id = 0
		self.code = 0
		self.player_time = 0
		# bool
		self.verified = []
		self.langue = [0, ""]
		# string
		self.name = ""
		self.platform = ""
		# Threads
		self.dummy_timer = threading.Timer(20, self.close)
		self.dummy_timer.start()
		# Open mysql
		self.mysql = server.mysql

	def handle_close(self):
		if self.address[0] in self.server.connections:
			self.server.connections[self.address[0]] -= 1
			if self.server.connections[self.address[0]] == 0:
				del self.server.connections[self.address[0]]
		self.close()

	def handle_read(self):
		try:
			data = self.recv(8192)
		except: 
			data = ''
		if data == '':
			return None
		elif data == b'<policy-file-request/>\x00':
			self.send(b"<cross-domain-policy><allow-access-from domain=\"*\" to-ports=\"*\" /></cross-domain-policy>")
			self.close()
		else:
			manager.parser(self, handler.process(data))