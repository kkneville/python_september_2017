class Underscore(object):
	def map(self, foo, sequ):
		list = []
		for item in sequ:
			list.append(foo(item))
		return list	

	def reduce(self, foo, sequ, initial=None):
		if len(sequ) >0:
			result = sequ[0] if initial == None else initial
			for item in range(1 if initial == None else 0,len(sequ)):
				result = foo(result, sequ[item])
			return result
		return

	def filter(self, foo, sequ):
		result = [] if type(sequ)== list else "" if type(sequ) == str else ()
		for item in sequ:
			if foo != None:
				if(foo(item)):
					result += [item] if type(sequ)== list else item if type(sequ) == str else (item,)
			else:
				if item == True:
					result += [item] if type(sequ)== list else item if type(sequ) == str else (item,)
		return result
	
	def reject(self, foo, sequ):
		result = [] if type(sequ)== list else "" if type(sequ) == str else ()
		for item in sequ:
			if foo != None:
				if not foo(item):
					result += [item] if type(sequ)== list else item if type(sequ) == str else (item,)
			else:
				if item == False:
					result += [item] if type(sequ)== list else item if type(sequ) == str else (item,)
		return result
	
	def find(self, foo, sequ):
		for num in range(len(sequ)):
			if foo(sequ[num]):
				return num
		else:
			return -1

#===========
# Main 
#===========	
	
_ = Underscore()

print("map",_.map((lambda x: x+x), "Hello"))
print("reduce",_.reduce((lambda x,y: x + y),"abcd"))
print("reject",_.reject((lambda x: x%2 == 0),[0,1,2,3,4,5]))
print("filter",_.filter((lambda x: x%2 == 0),[0,1,2,3,4,5]))

print("find", _.find((lambda x: x == "k"), "abcdekgasdfl;kj"))

