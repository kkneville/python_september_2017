class Store(object):
	def __init__(self, location, owner):
		self.product = []
		self.location = location
		self.owner = owner
		print 'store exists'

	def add_product(self, item):
		self.product.append(item)
		print self.product

	def remove_product(self, item):
		self.product.remove(item)

	def inventory(self):
		for item in self.product:
			item.print_me()
		# print 'created'

class Product(object):
	def __init__(self, name, price):
		self.name = name
		self.price = price
		print 'item has been made'

	def print_me(self):
		print self.name, self.price


bananas = Product('chiquita', .99)
apples = Product('green', 5)
pies = Product('pumpkin', 15)
print '***************************'

store1 = Store('Dallas', 'Campy')

print '***************************'
store1.add_product(bananas)		
store1.add_product(apples)		
store1.add_product(pies)		


print '***************************'
# store1.add_product('tilex')
# store1.add_product('chili')
# store1.add_product('cocaine')
# store1.add_product('goldfish')

# # store1.remove_product('Donuts')
# store1.inventory()

# store1.remove_product('cocaine')

store1.inventory()


# print store1.product

#kyle and Campy worked on this together

