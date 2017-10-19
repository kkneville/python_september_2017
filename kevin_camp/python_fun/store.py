class Store(object):
	def __init__(self, location, owner):
		self.product = []
		self.location = location
		self.owner = owner

	def add_product(self, item):
		self.product.append(item)

	def remove_product(self, item):
		self.product.remove(item)

	def inventory(self):
		print self.product

		print 'created'

store1 = Store('Dallas', 'Campy')

store1.add_product('apples')
store1.add_product('pies')
store1.add_product('tylex')
store1.add_product('chili')
store1.add_product('cocaine')
store1.add_product('goldfish')

# store1.remove_product('Donuts')
store1.inventory()

store1.remove_product('cocaine')

store1.inventory()


# print store1.product
