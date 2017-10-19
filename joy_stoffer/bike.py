class Bike(object):
        def __init__(self, price, max_speed, miles = 0):
            self.price = price
            self.max_speed = max_speed
            self.miles = miles

        def displayInfo(self):
            print 'Price is :$'+ str(self.price)
            print 'Maximum Speed:' + str(self.max_speed) +'mph'
            print 'Total Miles:' + str(self.miles) + ' miles'
            return self

        def ride(self):
            self.miles += 10
            print 'riding on and rode ' + str(self.miles)
            return self
    #if you reverse less
        def reverse(self):
            if self.miles > 5:
                self.miles -= 5
                print 'Had to go back... now total miles is ' + str(self.miles)
                return self
            else:
                self.miles -= 0
                print 'Flat tire, day over'
            return self

print 'Bike One'
bike1 = Bike('2000','15')
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

print 'Bike Two'
bike2 = Bike('1500', '13')
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

print 'Bike Three'
bike3 = Bike('1000', '10')
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
