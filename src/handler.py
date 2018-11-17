from src.buffer.Buffer import *

class handler:
	@staticmethod
	def process(data=str):
		buffer = Buffer(data)
		length = len(data)
		if length <= 0xFF:
			idata = buffer.readInt8()
			ldata = buffer.readInt8()
		elif length <= 0xFFFF:
			idata = buffer.readInt8()
			ldata = buffer.readInt16()
		elif length <= 0xFFFFFF:
			idata = buffer.readInt8()
			ldata = (buffer.readInt8() << 16)
			ndata = (buffer.readInt8() << 8)
			ydata = buffer.readInt8()
		return buffer