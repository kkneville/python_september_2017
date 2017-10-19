def dic_to_tup(dict):
	tup = ()
	for key,val in dict.items():
		tup+=(key,val)
	return tup
	

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
print(dic_to_tup(my_dict))