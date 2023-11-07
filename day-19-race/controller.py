def start(starting_point, pen):
    pen.up()
    pen.goto(starting_point)
    pen.left(90)

def paint(data, start_x, end_x, start_y, pen, color):
    pen.color(color)
    lit = 0
    for x in range(int(start_x), int(end_x)):
        pen.down()
        pen.forward(data[lit])
        lit += 1
        pen.up()
        pen.goto(x + 1, start_y)

def delete_bar(end_y, pen, start_x, start_y):
    pen.goto(start_x, start_y)
    pen.color("white")
    pen.down()
    pen.forward(end_y)
    pen.up()
    pen.left(180)
    pen.forward(end_y)
    pen.left(180)

def paint_bar(end_y, pen, color, start_x, start_y):
    pen.goto(start_x, start_y)
    pen.color(color)
    pen.down()
    pen.forward(end_y)
    pen.up()
    pen.left(180)
    pen.forward(end_y)
    pen.left(180)
