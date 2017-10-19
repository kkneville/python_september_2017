# try this either as a .py file or in the python shell
import turtle
# the distance we want the pointer to travel each time
DIST = 20
for x in range(0,6):
	print ("x {}".format(str(x)))
	for y in range(1,5):
		print ("y {}".format(str(y)))
		# turn the pointer 90 degrees to the right
		turtle.right(90)
		# advance according to set distance
		turtle.forward(DIST)
		# add to set distance
		DIST += 5

#not enough turtle in this program so i fixed it
turtle.right(90)
for i in range(2):
	turtle.forward(DIST/5)
	turtle.left(90)
	turtle.forward(15)
	turtle.right(90)
	turtle.forward(DIST/5)
	turtle.right(90)
	turtle.forward(15)
	turtle.left(90)
turtle.forward(DIST/5)
turtle.right(90)
turtle.forward(DIST/2)
turtle.left(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(3)
turtle.right(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(DIST/2 -3)
turtle.right(90)
for i in range(2):
	turtle.forward(DIST/5)
	turtle.left(90)
	turtle.forward(15)
	turtle.right(90)
	turtle.forward(DIST/5)
	turtle.right(90)
	turtle.forward(15)
	turtle.left(90)
turtle.forward(DIST/5)
turtle.right(90)
DIST+=5
turtle.forward(DIST/3)
turtle.left(90)
turtle.forward(DIST/3)
turtle.right(90)
turtle.forward(DIST/3)
turtle.right(90)
turtle.forward(DIST/3)
turtle.left(90)
turtle.forward(DIST/3)
