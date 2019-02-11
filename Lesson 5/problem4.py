from turtle import *

mia = Turtle()

mia.color('blue')
mia.pensize(6)
mia.speed(8)
mia.shape('turtle')

def drawHexagon(side):
	for x in range(6):
		mia.forward(side)
		mia.left(60)

drawHexagon(10)
drawHexagon(20)
drawHexagon(30)
drawHexagon(40)
drawHexagon(50)
drawHexagon(60)
drawHexagon(70)
drawHexagon(80)
drawHexagon(90)


mainloop()