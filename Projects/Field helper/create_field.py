import random

def create(width, heigth):
    sideA = random.randint(0, width)
    sideB = random.randint(0, heigth)
    field = [sideA, sideB]
    return field

def paint(pen, field):
    sideA = field[0]
    sideB = field[1] 

    pen.up()
    pen.goto(sideA / 2 * (-1), sideB  / 2 * (-1))
    pen.down()

    for _ in range(4):

        if _ % 2 != 0:
            pen.forward(sideB)
        else:
            pen.forward(sideA)  

        pen.left(90)
    
    pen.up()
    pen.goto(0, 0)