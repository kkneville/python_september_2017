output = ""
for y in range(8):
	for x in range(4):
		if y % 2 == 0:
			output+= "* "
		else:
			output+= " *"
	output+= "\n"
print(output)