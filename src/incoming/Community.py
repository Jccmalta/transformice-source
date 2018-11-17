from utils.language import *

class RCommunity:
	@staticmethod
	def get(client, tokens, buffer):
		if tokens == [8, 2]:
			langue_id = buffer.readInt8()
			cant = buffer.readInt8()
			if langue_id > 32:
				langue_id = 0
			client.langue[0] = langue_id
			client.langue[1] = Language.langue_by_id(langue_id)
			client.verified.append(True)
			return True
		return