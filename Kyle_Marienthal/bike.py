class Bike(object):
	"""docstring for Bike"""
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print self.price, self.max_speed, self.miles

	def ride(self):
		print "driving"
		self.miles += 10

	def reverse(self):
		print "reversing"
		self.miles -= 5
		

bike1 = Bike(15, 50)
bike2 = Bike(20, 200)
bike3 = Bike(25, 400)

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()