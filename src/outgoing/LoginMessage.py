from src.buffer.Buffer import *

class SLoginMessage:
	@staticmethod
	def send(client, id=int, msg1=str, msg2=str):
		buffer = Buffer()
		buffer.writeInt8(26)
		buffer.writeInt8(12)
		buffer.writeInt8(id)
		buffer.writeString(msg1)
		buffer.writeString(msg2)
		buffer.crypto_simple()
		client.send(buffer.toString().encode())