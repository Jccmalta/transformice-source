from src.outgoing.CorrectVersion import *

class RCorrectVersion:
	@staticmethod
	def get(client, tokens, buffer):
		if tokens == [28, 1]:
			version = buffer.readInt16()
			ckey = buffer.readString().decode()
			player_type = buffer.readString().decode()
			cain = buffer.readString().decode()
			win_id = buffer.readInt32()
			pc_str = buffer.readString().decode()
			server_str= buffer.readString().decode()
			computer_str = buffer.readString().decode()
			id_gain = buffer.readInt32()
			lip = buffer.readInt32()
			x = buffer.readString().decode()
			if version != client.server.config["version"]:
				client.close()
			elif ckey != client.server.config["ckey"]:
				client.close()
			else:
				client.verified.append(True)
				SCorrectVersion.send(client)
				return True
		return