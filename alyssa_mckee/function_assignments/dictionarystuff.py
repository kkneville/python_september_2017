me = {"name": "Alyssa", "age":23, "country of birth": "United States", "favorite_language": "Java"}

def print_dict(person):
	for key,value in person.items():
		print("My {} is {}".format(key, value))
		
print_dict(me)