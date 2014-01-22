import datetime

class point:

	def __init__(self,latitude,longitude,timestamp):
		self.latitude = float(latitude)
		self.longitude = float(longitude)
		self.timestamp = timestamp

	def display(self):
		print "latitude : " + str(self.latitude) + "\r\n"\
		+ "longitude : " + str(self.longitude) + "\r\n"\
		+ "timestamp : " + str(self.timestamp) + "\r\n"


