class Bike(object):
	def __init__(self, price, speed):
		self.price = price
		self.max_speed = speed
		self.miles = 0
	
	def displayInfo(self):
		print("The price is {} \nThe maximum speed is {} \nTotal miles ridden: {}".format(self.price, self.max_speed, self.miles))
	
	def ride(self):
		print("Riding")
		self.miles += 10
		return self
	
	def reverse(self):
		if self.miles<5:
			print ("can't reverse")
			return self
		print("Reversing")
		self.miles -=5
		return self
		
my_bike = Bike(50, 20)
your_bike = Bike(40, 15)
noones_bike = Bike(100, 100)

my_bike.ride().ride().ride().reverse().displayInfo()
your_bike.ride().ride().reverse().reverse().displayInfo()
noones_bike.reverse().reverse().reverse().displayInfo()