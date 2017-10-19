the_list = ['magical unicorns',19,'hello',98.98,'world']
sum = 0
string = ""
for val in the_list:
	if type(val) is str:
		string+= val + " "
	if type(val) is int or type(val) is float:
		sum+=val

if(len(string) != 0 and sum != 0):
	print("the list you entered is of mixed type")
elif(len(string) == 0):
	print("the list you entered is of Number type")
else:
	print("the list you entered is of String type")
	
if len(string) != 0:
	print("String: " + string)
if sum != 0:
	print("Sum: "+ str(sum))