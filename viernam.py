#vietnam flag using python
import turtle
from turtle import *

setup(450, 350)
speed(1)
penup()
goto(-55,25)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    forward(120)
    right(144)
end_fill()
bgcolor('red')
turtle.getscreen()._root.mainloop()