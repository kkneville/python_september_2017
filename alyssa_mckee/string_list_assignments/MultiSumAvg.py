#Multiples

#prints all odd numbers from 1 to 1000
for i in range(1,1000,2):
  print(i)
  
#prints multiples of 5 from 5 to a million
for i in range(5,1000001, 5):
	print(i)


#Sum List
a = [1, 2, 5, 10, 255, 3]
sum = 0
for num in a:
	sum+=num

print(sum)

#Average List
#takes the sum from sum list algorithm above
avg = sum/len(a)
print(avg)