arr1 = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
arr2 = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
	new_dict = zip(arr1,arr2)
	return new_dict

print make_dict(arr1,arr2)