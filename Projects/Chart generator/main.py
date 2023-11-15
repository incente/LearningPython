from turtle import Turtle, Screen
from chart import dimensionsPOS, border

pen = Turtle()
#pen.speed("fastest")
#pen.ht()
pen.pensize(1)

my_screen = Screen()


x = 500
y = 300

dimensionsPOS(pen, x, y)
border(pen, x, y, "black", 2, 1)


my_screen.exitonclick()