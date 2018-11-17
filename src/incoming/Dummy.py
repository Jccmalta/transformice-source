import threading

class RDummy:
	@staticmethod
	def get(client, tokens, buffer):
		if tokens == [26, 26]:
			if client.dummy_timer != None:
				client.dummy_timer.cancel()
			client.dummy_timer = threading.Timer(20, client.close)
			client.dummy_timer.start()
			return True
		return