output = "x "

for i in range(1,13):
	output+="{:>4}".format(i)
output+= "\n"

for y in range(1,13):
	output+= "{:<2}".format(y)
	for x in range(1,13):
		output+= "{:>4}".format(x*y)
	output+= "\n"

print(output)