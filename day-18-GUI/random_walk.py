from turtle import Turtle, Screen
import random

directions = [0, 90, 180, 270]

pen = Turtle()
pen.pensize(10)
pen.speed("fastest")
Screen().colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def walk(color):
    pen.color(color)
    pen.left(random.choice(directions))
    pen.forward(20)

for _ in range(500):
    walk(random_color())

screen = Screen()
screen.exitonclick()