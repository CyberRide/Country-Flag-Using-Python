import turtle
from turtle import *

speed(2)
setup(750, 500)
screen = turtle.Screen()
t = turtle.Turtle()

t.penup()
t.goto(-390, 260)
t.pendown()

t.color("black")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()

t.left(90)

t.color("white")
t.begin_fill()
t.forward(10)
t.left(90)
t.forward(800)
t.left(90)
t.forward(10)
t.end_fill()

t.left(180)
t.penup()
t.forward(10)
t.pendown()

t.color("red")
t.begin_fill()
t.forward(167)
t.right(90)
t.forward(800)
t.right(90)
t.forward(167)
t.end_fill()

t.left(180)
t.penup()
t.forward(167)
t.pendown()

t.color("white")
t.begin_fill()
t.forward(10)
t.left(90)
t.forward(800)
t.left(90)
t.forward(10)
t.end_fill()

t.left(180)
t.penup()
t.forward(10)
t.pendown()

t.color("green")
t.begin_fill()
t.forward(167)
t.right(90)
t.forward(800)
t.right(90)
t.forward(167)
t.end_fill()

wn = turtle.Screen()
tr = turtle.Turtle()

wn.addshape('v.gif')
tr.shape('v.gif')
wn.mainloop()

t.hideturtle()
turtle.getscreen()._root.mainloop()