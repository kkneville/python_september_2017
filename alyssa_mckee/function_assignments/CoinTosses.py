import random
def coin_toss_5k():
	heads_tails_counter = [0,0]
	words = ["head", "tail"]
	print("Starting the Program!")
	for i in range(1,5001):
		flip = round(random.random())
		heads_tails_counter[flip] += 1
		print("Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(i,words[flip],heads_tails_counter[0], heads_tails_counter[1]))
	
coin_toss_5k()