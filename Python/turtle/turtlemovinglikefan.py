#concept usedd= screen generation, title making, shape, shapesize,pencolor,loop


import turtle

s=turtle.getscreen()
s.title("Turtle Moving Like A Fan")
t1=turtle.Turtle()
t1.shape("turtle")
t1.shapesize(10,10,5)            #(length,breath,boundary)
t1.pencolor("Blue")

for angle in range(0,901,90):
    t1.left(angle)
    
turtle.done()