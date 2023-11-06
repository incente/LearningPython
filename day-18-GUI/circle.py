from turtle import Turtle, Screen
import random


pen = Turtle()
pen.speed("fastest")
Screen().colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def circle(color):
    pen.color(color)
    pen.circle(100)
    pen.left(2)

for _ in range(180):
    circle(random_color())


screen = Screen()
screen.exitonclick()