class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100
		# print 'animal created, name: {}, health: {}'.format(self.name, self.health) 

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def display_health(self):
		print 'im a dog , my name is' + self.name
		print 'i have ' + str(self.health) + ' health left'


class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150

	def pet(self):
		self.health += 5
		return self


class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170

	def fly(self):
		self.health -= 10

	def display_health(self):
		print 'I am a Dragon'
		super(Dragon, self).displayHealth()




dog = Dog('Fido')
# dog.walk().walk().walk().run().run().display_health()
# dog.walk().walk().walk().run().pet().display_health()
