val = 455

def filter_by_type(val):
	if type(val) is int:
		if val>=100:
			print("That's a big number!")
		else:
			print("That's a small number")


	if type(val) is str:
		if len(val) >= 50:
			print("Long Sentence")
		else:
			print("Short Sentance")

	if type(val) is list:
		if len(val) >= 10:
			print("Big list!")
		else:
			print("Short list")

sI = 45
print(sI)
filter_by_type(sI)

mI = 100
print(mI)
filter_by_type(mI)

bI = 455
print(bI)
filter_by_type(bI)

eI = 0
print(eI)
filter_by_type(eI)

spI = -23
print(spI)
filter_by_type(spI)

sS = "Rubber baby buggy bumpers"
print(sS)
filter_by_type(sS)

mS = "Experience is simply the name we give our mistakes"
print(mS)
filter_by_type(mS)

bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
print(bS)
filter_by_type(bS)

eS = ""
print(eS)
filter_by_type(eS)

aL = [1,7,4,21]
print(aL)
filter_by_type(aL)

mL = [3,5,7,34,3,2,113,65,8,89]
print(mL)
filter_by_type(mL)

lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
print(lL)
filter_by_type(lL)

eL = []
print(eL)
filter_by_type(eL)

spL = ['name','address','phone number','social security number']
print(spL)
filter_by_type(spL)