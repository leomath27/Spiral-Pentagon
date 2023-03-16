import turtle
t = turtle.Turtle()

t.speed(0)
#sets the pen color to magenta
t.pencolor("magenta")
#makes the turtle move left by 120 degrees
t.left(120)
#sets the background color
turtle.bgcolor("black")
#initializze variable k as the incrementation of the size
k=2

# Loop 85 times to draw all the pentagons
for i in range(85):
    # Calculate the size of the pentagon for this iteration
    size = 10 + k
    # Call the function to draw the pentagon
    for j in range(6):
        # Move forward by the specified size
        t.forward(size)
        # Turn right by 72 degrees
        t.right(72)
    # Turn right by 1 degree after each iteration
    t.right(1)
    #incrementation by 4 units
    k+=4

# Hide the turtle so it doesn't show up in the final image
t.hide()
# Keep the turtle window open until the user closes it
t.done()
