#Ghana Flag Using Python
#Author: CyberRide
from traceback import format_exc
import turtle
from turtle import *

setup(800, 500)
speed(0)

penup()
goto(-55,25)
pendown()
color("black")
begin_fill()
for i in range(5):
    forward(120)
    right(144)
end_fill()

penup()
goto(-400,250)
pendown()
color("red")
begin_fill()
for i in range(2):
    forward(800)
    right(90)
    forward(167)
    right(90)
end_fill()


penup()
goto(-400, -250)
pendown()
color("green")
begin_fill()
for i in range(2):
    forward(800)
    left(90)
    forward(167)
    left(90)
end_fill()

bgcolor("gold")
hideturtle()
turtle.getscreen()._root.mainloop()