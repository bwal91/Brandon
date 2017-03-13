class Bike(object):
	def __init__(self, max_speed, price):
		self.max_speed = max_speed
		self.price = price
		self.miles = 0

	def displayInfo(self):
		print self.max_speed
		print self.price
		return self

	def ride(self):
		self.miles += 10
		print "Riding"+" "+ str(self.miles)
		return self


	def reverse(self):
		self.miles -=10
		print "Riding"+" "+ str(self.miles)
		return self


blue=Bike('Max Speed: 25mph', 'Cost: $200')
blue.ride().ride().ride().reverse().displayInfo()
red=Bike('Max Speec: 15mph', 'Cost: $100')
red.ride().ride().reverse().reverse().displayInfo()
purple=Bike('Max Speed: 50mph', 'Cost: $500')
purple.reverse().reverse().reverse().displayInfo()
