list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

if len(list_one) != len(list_two):
	print("the lists are not the same")
else:
	for i in range(len(list_one)):
		if list_one[i] != list_two[i]:
			print("the lists are not the same")
			break
	else:
		print("The lists are the same")