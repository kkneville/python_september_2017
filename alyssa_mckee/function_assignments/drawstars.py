#because it makes sense to me that if someone just wanted one row of stars, they shouldn't have to make an array with only one value, just pass in a single number instead
def draw_stars(num_or_arr):
	if(type(num_or_arr) == int):
		print("*"*num_or_arr)
		return
	if(type(num_or_arr) == list):
		for i in num_or_arr:
			if(type(i) == int):
				print("*"*i)
			else:
				print(i[0].lower()*len(i))
draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])