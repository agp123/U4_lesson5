from turtle import *

mia = Turtle()

mia.color('blue')
mia.pensize(6)
mia.speed(8)
mia.shape('turtle')

def drawStar():
	for x in range(5):
		mia.forward(100)
		mia.left(144)

mia.penup()
mia.goto(0,0)
mia.pendown()
drawStar()

mia.penup()
mia.goto(200,0)
mia.pendown()
drawStar()


mia.penup()
mia.goto(-200,0)
mia.pendown()
drawStar()


mainloop()