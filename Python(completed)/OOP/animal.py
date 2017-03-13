class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print "Name:" + " " + self.name
		print "Health:" + " " + str(self.health)
		return self
# animal=Animal('Brandon')
# animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150
	def pet(self):
		self.health += 5
		return self
# dog=Dog('Hello')
# dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170
	def fly(self):
		self.health -= 10
		return self
	def displayHealth(self):
		print "This Is A DRAGON!"
		super(Dragon, self).displayHealth()

drag=Dragon('Toothless')
drag.walk().walk().walk().run().run().fly().fly().displayHealth()