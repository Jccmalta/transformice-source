class utils:
	@staticmethod
	def match(string=str):
		characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '.', '_', '-', '+']
		for s in list(string):
			if not s.lower() in characters or not s.upper() in characters:
				return True
		return False