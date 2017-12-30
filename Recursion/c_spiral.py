from turtle import *

my_turtle = Turtle()
my_win = Screen()

def draw_spiral(my_turtle ,line_len): 
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(91)
        draw_spiral(my_turtle, line_len - 2)
draw_spiral(my_turtle,300)
my_win.exitonclick()
