# Inheiritance: gain the same methods and attributes as another class (is a)
# Composition: have other classes/objects (has a)

class Animal(object):  #PascalCase
    def __init__(self, name, color): # = in aruguments means default value
        self.name = name
        self.color = color

class Dog(Animal):
    def __init__(self, name, color, legs=4):
        super(Dog, self).__init__(name, color)
        self.legs = legs
        self.personality = "Happy"

class Toy(object):
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name, color, legs=4):
        super(Cat, self).__init__(name, color)
        self.legs = legs
        self.personality = "Cranky"
        self.toys = []

    def add_toy(self, toy):
        self.toys.append(toy)

    def display_all_toys(self):
        for toy in self.toys:
            print toy.name

mittens = Cat('Mittens', 'black')

toy = Toy('ball')

mittens.add_toy(toy)

mittens.display_all_toys()


# print animaluno.personality


