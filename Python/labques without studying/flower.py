import turtle

def draw_petal(t):
    t.circle(100, 60)  # Draw a semicircle
    t.left(120)        # Turn left to draw the other half of the petal
    t.circle(100, 60)  # Draw the other semicircle
    t.left(120)        # Reset the turtle's direction

def draw_flower(t, petals):
    for _ in range(petals):
        draw_petal(t)
        t.left(360 / petals)  # Rotate to position for the next petal

def main():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")  # Set background color

    t = turtle.Turtle()
    t.color("red")  # Set color for the petals
    t.speed(10)     # Set the speed of drawing

    draw_flower(t, 8)  # Draw a flower with 8 petals

    t.hideturtle()  # Hide the turtle
    turtle.done()   # Finish the drawing

if __name__ == "__main__":
    main()