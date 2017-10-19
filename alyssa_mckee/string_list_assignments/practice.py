words = "It's thanksgiving day. It's my birthday,too!"
print (words.find("day"))

day_to_month = words.replace("day", "month")
print (day_to_month)

x = [2,54,-2,7,12,98]

print (min(x))
print (max(x))

x = ["hello",2,54,-2,7,12,98,"world"]

print(x[0])
print(x[len(x)-1])

first_and_last = [x[0], x[len(x)-1]]
print(first_and_last)

x = [19,2,54,-2,7,12,98,32,10,-3,6]

sorted_x = sorted(x)

NewList = [sorted_x[:int(len(sorted_x)/2)]]
NewList.extend(sorted_x[int(len(sorted_x)/2):])
print(NewList)