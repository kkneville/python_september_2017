class Product(object):
	def __init__(self, price, item_name, weight, brand, cost, status="for sale"):
		self.price = price
		self.name = item_name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = status
	
	def sell(self):
		self.status = "sold"
		return self
	
	def add_tax(self, tax):
		return format(self.price + self.price*tax, '.2f')
	
	def return_item(self, reason):
		reason = reason.lower()
		if reason.find("defective") > -1:
			self.status = "defective"
			self.price = 0
		if .find("like new") > -1:
			self.status = "for sale"
		if reason.find("opened") > -1:
			self.status = "used"
			self.price = self.price*.80
		return self
	
	def display_info(self):
		print("Name: {} \nPrice: ${} \nWeight: {}lb \nBrand: {} \nCost: ${} \nStatus: {}".format(self.name, self.price, self.weight, self.brand, self.cost, self.status))
		return self

ball = Product(2,"ball", ".5", "Hasbro", .25)
ball.display_info()
print(ball.add_tax(.0825))
print()
ball.sell().display_info()
print()
ball.return_item("opened the box, it was the wrong color").display_info()