from turtle import *

mia = Turtle()

mia.color('blue')
mia.pensize(6)
mia.speed(10)
mia.shape('turtle')

def drawtriangle():
	for x in range (3):
		mia.forward(100)
		mia.left(120)

for x in range(18):
	drawtriangle()
	mia.left(30)

mainloop()