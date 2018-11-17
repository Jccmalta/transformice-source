from src.incoming.CorrectVersion import *
from src.incoming.Community import *
from src.incoming.ComputerInfo import *
from src.incoming.Dummy import *
from src.incoming.Login import *
from utils.echo import *

class manager:
	@staticmethod
	def parser(client, buffer):
		id = buffer.readInt8()
		tokens = [buffer.readInt8(), buffer.readInt8()]
		echo.log("{0} - Recv: - Tokens: {1}: - {2}".format(client.address[0], tokens, repr(buffer.toString())))

		if client.packet_id != id:
			client.close()
		else:
			client.packet_id += 1 % 100

		handlers = [RCorrectVersion, RCommunity, RComputerInfo, RDummy, RLogin]
		for handler in handlers:
			if handler.get(client, tokens, buffer):
				return
				
		echo.log("{0} - New: - Tokens: {1}: - {2}".format(client.address[0], tokens, repr(buffer.toString())))
