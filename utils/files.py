class files:
	@staticmethod
	def read(dic=""):
		file = open(dic, "r")
		value = file.read()
		file.close()
		return value

	@staticmethod
	def write(dic="", value=str):
		file = open(dic, "w")
		file.write(str(value))
		file.close()