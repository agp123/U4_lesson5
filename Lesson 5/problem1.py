from turtle import *

mia = Turtle()

mia.color('blue')
mia.pensize(6)
mia.speed(8)
mia.shape('turtle')

for x in range(3):
	mia.forward(100)
	mia.left(120)

mainloop()