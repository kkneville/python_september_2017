class Car(object):
	def __init__(self, price, speed, fuel, milage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = milage
		if price>10000:
			self.tax = .15
		else:
			self.tax = .12
	
	def display_all(self):
		return "Price: {}\nSpeed: {}\nFuel: {}\nMileage: {}\nTax: {}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)
	
my_car = Car(9000, 40, "half full", "22mpg")
his_car = Car(13700, 60, "practically empty", "20mpg")
her_car = Car(12000, 50, "full", "18mpg")
free_car = Car(0, 3, "empty", "5")
electric_car = Car(16000, 60, "none", "100mpg-e")
dream_car = Car(5000, 100, "full", "50mpg")

print(my_car.display_all()+"\n")
print(his_car.display_all()+"\n")
print(her_car.display_all()+"\n")
print(free_car.display_all()+"\n")
print(electric_car.display_all()+"\n")
print(dream_car.display_all()+"\n")
