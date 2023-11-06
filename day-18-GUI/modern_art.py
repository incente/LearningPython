from turtle import Turtle, Screen
import random



pen = Turtle()
pen.speed("fastest")
pen.pensize(20)
Screen().colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def paint():
    pen.penup()
    pen.setpos(-410, 300)

    def row():
        for _ in range(16):
            pen.pencolor(random_color())
            pen.pendown()
            pen.forward(1)
            pen.penup()
            pen.forward(50)

    def next(x):
        pen.left(x)
        pen.forward(50)
        pen.left(x)

    for _ in range(13):
        row()
        if _ % 2 == 0:
            next(270)
        else:
            next(90)
    

paint()

screen = Screen()
screen.exitonclick()