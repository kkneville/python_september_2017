
import time
start_time = time.time()
counter = 0
found_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for num in range(100, 100001):
	for x in found_primes:
		counter+=1
		if num%x == 0:
			break
		if x*2 > num:
			break
	else:
		found_primes.append(num)
		print("Foo")
		continue

	last_digit = int(str(num)[len(str(num))-1])
	if (last_digit != 2 and last_digit != 3 and last_digit != 7 and last_digit != 8) and (num %4 == 0 or num%4 == 1) and (num%3 ==0 or num%3 ==1):
		x = 10
		while x*x <= num:
			counter+=1
			
			if x*x == num:
				print("Bar")
				break
			x+=1
		else:
			print("FooBar")
	else:
		print("FooBar")
			
	
print("for itterations: {}".format(counter))
print("{} seconds".format(time.time()-start_time))