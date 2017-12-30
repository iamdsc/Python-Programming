# Implementing Fractal tree
import turtle

def tree(branch_len, t):
    if branch_len>0: # Base Case
        t.forward(branch_len)
        t.right(25)
        tree(branch_len - 13, t)
        t.left(50)
        tree(branch_len - 13, t)
        t.right(25)
        t.backward(branch_len)
def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(90,t)
    my_win.exitonclick()

main()
