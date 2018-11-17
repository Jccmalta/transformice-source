from utils.language import *

class RComputerInfo:
	@staticmethod
	def get(client, tokens, buffer):
		if tokens == [28, 17]:
			computer_langue = buffer.readString()
			computer_op = buffer.readString()
			computer_version = buffer.readString()
			computer_pol = buffer.readInt8()
			client.verified.append(True)
			return True
		return