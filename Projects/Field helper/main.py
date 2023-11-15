from turtle import Turtle, Screen
from create_field import create, paint
from assistant import scan

pen = Turtle()
#pen.speed("fastest")
#pen.ht()

my_screen = Screen()

field = create(my_screen.window_width(), my_screen.window_height())
paint(pen, field)
scan(pen, field, 10)


my_screen.exitonclick()