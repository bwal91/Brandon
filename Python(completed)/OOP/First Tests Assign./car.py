class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price=price
		self.speed=speed
		self.fuel=fuel
		self.mileage=mileage
		if (self.price>10000):
			self.tax= self.price*.15
		else:
			self.tax=self.price*.12

	def display_all(self):
		print "Car:"
		print "Price:"+" " + str(self.price)
		print "Speed:"+" "+ str(self.speed)
		print "Fuel:"+" "+ str(self.fuel)
		print "Mileage:"+" "+ str(self.mileage)
		print "Tax:" + " " + str(self.tax)



car1=Car(15000, '100mph', 'Full', '50mpg')
car1.display_all()
car2=Car(12000, '80mph', 'Half Full', '45mpg')
car2.display_all()
car3=Car(55000, '150mph', 'Full', '20mpg')
car3.display_all()
car4=Car(22000, '95mph', 'Empty', '34mpg')
car4.display_all()
car5=Car(150000, '125mph', 'Dude', '75mpg')
car5.display_all()
car6=Car(8000, '65mph', 'Broke', '12mpg')
car6.display_all()