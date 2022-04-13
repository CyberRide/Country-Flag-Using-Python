import turtle
from turtle import *
wn = turtle.Screen()
wn.bgcolor("gold")
turtle = turtle.Turtle()
turtle.speed(2)
turtle.penup()
turtle.shape("turtle")
setup(700, 500)
def drawFillRectangle(x, y, length, width, color):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def drawGreen() :
    x = -330
    y =  220
    color = 'dark green'
    drawFillRectangle(x, y, 440, 80, color)

def drawOrange() :
    x = -250
    y =  220
    color = 'dark orange'
    drawFillRectangle(x, y, 440, 80, color)

def drawbrown() :
    x = -130
    y =  220
    
    color = 'brown'
    drawFillRectangle(x, y, 440, 450, color)


            
drawGreen()
drawOrange()
drawbrown()
wn.addshape('v.gif')
turtle.shape('v.gif')
turtle.goto(100, 10)
turtle.stamp()
wn.mainloop()
# wn = turtle.Screen()
# tr = turtle.Turtle()



turtle.getscreen()._root.mainloop()