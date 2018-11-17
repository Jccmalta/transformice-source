from src.outgoing.LoginMessage import *
from utils.utils import *

class RLogin:
	@staticmethod
	def get(client, tokens, buffer):
		if tokens == [26, 8]:
			if len(client.verified) >= 3:
				player_name = buffer.readString().decode()
				hash_pass = buffer.readString().decode()
				url = buffer.readString()
				room_name = buffer.readString().decode()
				login_xor = buffer.readInt32()
				bit_xor = buffer.readInt8()
				name_lop = buffer.readString().decode()
				if utils.match(player_name):
					SLoginMessage.send(client, 6)
				elif player_name in client.server.users_online:
					SLoginMessage.send(client, 1)
				elif len(player_name) > 12:
					SLoginMessage.send(client, 4)
				elif player_name == "" or hash_pass == "":
					client.name = '*{0}'.format(player_name)
					x=0
					while not client.name in client.server.users_online:
						x+=1
						client.name = '*{0}{1}'.format(client.name, x)
					client.id = 0
					client.server.last_code += 1
					client.code = client.server.last_code

				else:
					SLoginMessage.send(client, 2)
			return True
		return