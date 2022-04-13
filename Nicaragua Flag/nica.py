import turtle
from turtle import *

setup(800, 500)
speed(0)


penup()
goto(-400, 250)
pendown()
color('blue')
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
color('blue')
begin_fill()
for i in range(2):
    forward(800)
    left(90)
    forward(167)
    left(90)
end_fill()


turtle.getscreen()._root.mainloop()