def print_students_1(dictlist):
	for person in dictlist:
		print(person["first_name"],person["last_name"])
		
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
print_students_1(students)

def print_users(users):
	for key,val in users.items():
		print(key)
		count = 1
		for person in val:
			print("{} - {} {} - {}".format(count, person["first_name"], person["last_name"], len(person["first_name"]) + len(person["last_name"])))
			count+=1

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
print_users(users)