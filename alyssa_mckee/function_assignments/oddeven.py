def odd_even():
	states = ["even", "odd"]
	for num in range(1,2001):
		print("Number is {}. This is an {} number.".format(num,states[num%2]))

odd_even()

def multiply(li, m):
	for i in range(len(li)):
		li[i]*=m
	return li

b = multiply([2,4,10,16], 5)
print (b)

def layered_multiples(arr):
	new_arr = []
	for i in range(len(arr)):
		new_arr.append([])
		for x in range(arr[i]):
			new_arr[i].append('1')
	return new_arr

x = layered_multiples(multiply([2,3,5],3))
print (x)

