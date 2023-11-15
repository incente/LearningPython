def scan(pen, field, size):
    sideA = field[0]
    sideB = field[1]
    square = sideA * sideB

    pen.goto(sideA / 2 * (-1), sideB / 2 - (size / 2))
    pen.down()
    pen.pensize(size)
    pen.pencolor("red")
    
    for _ in range(int((sideB / size) / 2)):
        pen.forward(sideA)
        pen.left(270)
        pen.forward(size)
        pen.left(270)
        pen.forward(sideA)
        pen.left(90)
        pen.forward(size)
        pen.left(90)
