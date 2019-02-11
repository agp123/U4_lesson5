from turtle import *

mia = Turtle()

mia.color('blue')
mia.pensize(6)
mia.speed(8)
mia.shape('turtle')

for x in range(6):
	mia.forward(80)
	mia.left(60)

mainloop()