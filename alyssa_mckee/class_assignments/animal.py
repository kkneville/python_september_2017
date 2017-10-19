class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
	def walk(self):
		self.health-=1
		return self
	def run(self):
		self.health-=5
		return self
	def display_health(self):
		print("{}'s health: {}".format(self.name, self.health))
		return self

class Dog(Animal):
	def __init__(self, name, health=150):
		super(Dog, self).__init__(name, health)
	def pet(self):
		self.health+=5
		return self

class Dragon(Animal):
	def __init__(self, name, health=170):
		super(Dragon, self).__init__(name, health)
	def fly(self):
		self.health-=10
		return self
	def display_health(self):
		super(Dragon, self).display_health()
		print("I AM A DRAGON")
	
	
ani = Animal("it", 20)
ani.walk().walk().walk().run().run().display_health()

		
myDog = Dog("Sir Arthur")
myDog.walk().walk().walk().run().run().pet().display_health()

smaug = Dragon("Smaug", 1000000)
smaug.display_health()

#ani.fly()
#myDog.fly()