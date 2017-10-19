# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# for student in students:
# 	print student['first_name'] + ' ' + student['last_name']

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
for type, user in users.iteritems():
	count = 0
	print type
	for person in user:
		count += 1
		
		first_name = person['first_name'].upper()
		last_name = person['last_name'].upper()
		length = len(first_name) + len(last_name)
		print "{} - {} {} - {}".format(count, first_name, last_name, length)




