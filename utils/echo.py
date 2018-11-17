import time
class echo:
	@staticmethod
	def log(message=""):
		years = time.strftime("%Y")
		mouth = time.strftime("%m")
		days = time.strftime("%d")
		hours = time.strftime("%H")
		minutes = time.strftime("%M")
		seconds = time.strftime("%S")
		print('{0}/{1}/{2} {3}:{4}:{5} - {6}'.format(years, mouth, days, hours, minutes, seconds, message))