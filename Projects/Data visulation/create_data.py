import random

def dimensions(my_screen):

    height = my_screen.window_height()
    width = my_screen.window_width()
    bleed = 10
    start_x = (width / 2 * -1) + bleed
    start_y = (height / 2 * -1) + bleed
    end_x = (width / 2) - bleed
    end_y = height - bleed
    starting_point = (start_x, start_y)
    ending_point = (end_x, end_y)
    dimension = {"height": height,
                 "width": width,
                 "bleed": bleed,
                 "start_x": start_x,
                 "start_y": start_y,
                 "end_x": end_x,
                 "end_y": end_y,
                 "starting_point": starting_point,
                 "ending_point": ending_point}
    
    return dimension

def create(start_x, end_x, end_y):
    data = []
    for _ in range(int(start_x), int(end_x)):
        data.append(random.randint(0, end_y))
    return data