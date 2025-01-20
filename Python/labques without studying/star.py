import turtle

def draw_star(t):
    for _ in range(5):
        t.forward(100)  # Move the turtle forward by 100 units
        t.right(144)    # Turn the turtle right by 144 degrees

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")  # Set background color

    t = turtle.Turtle()
    t.color("red")  # Set color for the star
    t.speed(5)       # Set the speed of drawing

    draw_star(t)     # Draw the star

    t.hideturtle()   # Hide the turtle
    turtle.done()    # Finish the drawing

if __name__ == "__main__":
    main()