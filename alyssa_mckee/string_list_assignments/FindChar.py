def find_char(word_list, chr):
	new_list = []
	for v in word_list:
		if v.find(chr) >-1:
			new_list.append(v)
	print(new_list)

find_char(['hello','world','my','name','is','Anna'], 'o')
find_char(['hello','world','my','name','is','Anna'], 'z')
