import turtle
import Tkinter

for i in (0, 1000000000):
	turtle.forward(10)
	turtle.right(90)
	for i in (0, 1000000000):
		turtle.forward(10)
		turtle.right(45)


Tkinter.mainloop()
