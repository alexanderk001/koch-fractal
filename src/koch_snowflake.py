import turtle

def draw_koch_curve(turtle_obj, order, length):
    """Recursive function to draw the Koch curve."""
    if order == 0:
        turtle_obj.forward(length)
    else:
        segment_length = length / 3

        draw_koch_curve(turtle_obj, order - 1, segment_length)
        turtle_obj.left(60)
        draw_koch_curve(turtle_obj, order - 1, segment_length)
        turtle_obj.right(120)
        draw_koch_curve(turtle_obj, order - 1, segment_length)
        turtle_obj.left(60)
        draw_koch_curve(turtle_obj, order - 1, segment_length)

def draw_koch_snowflake(turtle_obj, order, length):
    """Draw the Koch snowflake by drawing three Koch curves."""
    for _ in range(3):
        draw_koch_curve(turtle_obj, order, length)
        turtle_obj.right(120)

# Initialize the turtle screen
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")

# Initialize the turtle
koch_turtle = turtle.Turtle()
koch_turtle.hideturtle()
koch_turtle.speed(0)
koch_turtle.penup()
koch_turtle.goto(-255, 150)
koch_turtle.pendown()
koch_turtle.pensize(2)
koch_turtle.color("deep sky blue")

# Parameters for the Koch snowflake
snowflake_order = 5
snowflake_length = 500

# Draw the Koch snowflake
draw_koch_snowflake(koch_turtle, snowflake_order, snowflake_length)

# Keep the window open until clicked
screen.exitonclick()
