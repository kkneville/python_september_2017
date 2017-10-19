def list_to_dic(list1,list2):
	dict = {}
	if len(list1)>len(list2):
		for i in range(len(list2)):
			dict[list1[i]] = list2[i]
			
	else:
		for i in range(len(list1)):
			dict[list1[i]] = list2[i]
	return dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print(list_to_dic(name,favorite_animal))