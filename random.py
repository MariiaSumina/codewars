import turtle
from random import choice

myTurtle = turtle.Turtle()
myColors = []
shapeColor = ""

myColor = ["blue", "pink", "#FFC0CB", "red", "green", "yellow"]

def drawSquare(pLength, pPen):
    myTurtle.pensize(10)
    myTurtle.pencolor(pPen)
    myTurtle.fillcolor(choice(myColor))
    myTurtle.begin_fill()
    myTurtle.forward (pLength)
    myTurtle.right (90)
    myTurtle.forward (pLength)
    myTurtle.right (90)
    myTurtle.forward (pLength)
    myTurtle.right (90)
    myTurtle.forward (pLength)
    myTurtle.end_fill()

drawSquare(100, 10)
myTurtle.home()
drawSquare(50, 10)
myTurtle.home()
drawSquare(25, 10)
myTurtle.home()