from turtle import Turtle, Screen
import create_data, controller, sorting

pen = Turtle()
pen.speed("fastest")
pen.ht()

my_screen = Screen()


original_data = create_data.create(create_data.dimensions(my_screen)["start_x"], 
                          create_data.dimensions(my_screen)["end_x"], 
                          create_data.dimensions(my_screen)["end_y"])

sorted_data = sorting.selection_sort_copy(original_data)

print(create_data.dimensions(my_screen))
print(original_data)
print(sorted_data)


def sorting_visualiation():
    controller.start(create_data.dimensions(my_screen)["starting_point"], pen)

    controller.paint(original_data, create_data.dimensions(my_screen)["start_x"], 
                 create_data.dimensions(my_screen)["end_x"], 
                 create_data.dimensions(my_screen)["start_y"], 
                 pen,
                 "black")
    
    for x in range(int(create_data.dimensions(my_screen)["start_x"]), int(create_data.dimensions(my_screen)["end_x"])):
            controller.delete_bar(create_data.dimensions(my_screen)["end_y"], pen, x, create_data.dimensions(my_screen)["start_y"])
            controller.paint_bar(create_data.dimensions(my_screen)["end_y"], pen, "black", create_data.dimensions(my_screen)["start_x"], create_data.dimensions(my_screen)["start_y"])


"""
def sorted_colors():
    controller.start(create_data.dimensions(my_screen)["starting_point"], pen)

    controller.paint(original_data, create_data.dimensions(my_screen)["start_x"], 
                    create_data.dimensions(my_screen)["end_x"], 
                    create_data.dimensions(my_screen)["start_y"], 
                    pen,
                    "blue")

    controller.paint(sorted_data, create_data.dimensions(my_screen)["start_x"], 
                    create_data.dimensions(my_screen)["end_x"], 
                    create_data.dimensions(my_screen)["start_y"], 
                    pen,
                    "red")
"""


sorting_visualiation()
#sorted_colors()


my_screen.exitonclick()