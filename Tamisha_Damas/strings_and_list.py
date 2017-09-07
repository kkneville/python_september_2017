string = "It's thanksgiving day It's my birthday, too!"
print string.find("day")
print string.replace("day", "month")

x = [2, 54, -2, 7, 12, 98]
print min(x)
print max(x)

a = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print a[0] +" "+ a[len(a)-1]

list_sort = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
print list_sort
list_sort.sort()
print list_sort

new_list = list_sort[:len(list_sort)/2]
new2_list = list_sort[len(list_sort)/2:]
print new_list
print new2_list
new2_list.insert(0,new_list)
print new2_list
