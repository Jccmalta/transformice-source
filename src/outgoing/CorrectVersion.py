from src.buffer.Buffer import *

class SCorrectVersion:
	@staticmethod
	def send(client):
		buffer = Buffer()
		buffer.writeInt8(26)
		buffer.writeInt8(3)
		buffer.writeInt32(0)
		buffer.writeInt8(client.packet_id)
		buffer.writeString(client.server.config["langue"])
		buffer.writeString(client.server.config["langue"])
		buffer.writeInt32(0)
		buffer.crypto_simple()
		client.send(buffer.toString().encode())