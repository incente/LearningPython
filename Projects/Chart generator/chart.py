def calibrate(pen):
    pen.up()
    pen.goto(0, 0)
    pen.pencolor("black")
    pen.pensize(1)

def null(point):
    nullpoint = point / 2 * (-1)
    return nullpoint

def dimensionsPOS(pen, x, y):

    null_x = null(x)
    null_y = null(y)
    pen.up()
    pen.goto(null_x, null_y)

    pen.down()
    pen.forward(x)
    pen.up()
    pen.goto(null_x, null_y)
    pen.left(90)
    pen.down()
    pen.forward(y)
    calibrate(pen)

def border(pen, x, y, color, type, size):

    def create(x, y, bleed):
        pen.pencolor(color)
        pen.pensize(size)
        pen.goto(null(x) - bleed, null(y) - bleed)
        pen.left(270)
        pen.down()
        pen.forward(x + bleed * 2)
        pen.left(90)
        pen.forward(y + bleed * 2)
        pen.left(90)
        pen.forward(x + bleed * 2)
        pen.left(90)
        pen.forward(y + bleed * 2)
        pen.left(180)
        calibrate(pen)
    
    bleed = size * 4
    for _ in range(type):
        create(x, y, bleed)
        bleed += bleed