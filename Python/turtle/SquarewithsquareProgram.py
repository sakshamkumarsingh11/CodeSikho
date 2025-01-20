#code is correct but incomplete

import turtle

s=turtle.getscreen()

t1=turtle.Turtle()

t1.ht()
t1.fillcolor("Light green")
t1.begin_fill()
t1.penup()
t1.goto(200,200)
t1.pendown()
t1.goto(-200,200)
t1.goto(-200,-200)
t1.goto(200,-200)
t1.goto(200,200)
t1.end_fill()
#now drawing smaller squares
#Could not understand to print more squares in 
turtle.done()





#somewhat the answer
"""
import turtle

# Set up the screen and turtle
s = turtle.getscreen()
t = turtle.Turtle()

def draw_square(x, y, size, color):
    ""
    Draws a square starting at (x, y) with a given size and color.
    ""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

# Draw the large green square
draw_square(-100, 100, 200, "green")

# Draw smaller squares in each quadrant
# Top-right quadrant
draw_square(0, 100, 100, "red")

# Top-left quadrant
draw_square(-100, 100, 100, "blue")

# Bottom-left quadrant
draw_square(-100, 0, 100, "yellow")

# Bottom-right quadrant
draw_square(0, 0, 100, "purple")

# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()
"""