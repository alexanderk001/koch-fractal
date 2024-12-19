import random
import turtle

def draw_random_koch_curve(turtle_obj, order, length):
    """Recursive function to draw the random Koch curve."""
    if order == 0:
        turtle_obj.forward(length)
    else:
        segment_length = length / 3
        random_direction = random.choice([-1, 1])

        draw_random_koch_curve(turtle_obj, order - 1, segment_length)
        turtle_obj.left(60 * random_direction)
        draw_random_koch_curve(turtle_obj, order - 1, segment_length)
        turtle_obj.right(120 * random_direction)
        draw_random_koch_curve(turtle_obj, order - 1, segment_length)
        turtle_obj.left(60 * random_direction)
        draw_random_koch_curve(turtle_obj, order - 1, segment_length)

def draw_random_koch_snowflake(turtle_obj, order, length):
    """Draw the random Koch snowflake by drawing three random Koch curves."""
    for _ in range(3):
        draw_random_koch_curve(turtle_obj, order, length)
        turtle_obj.right(120)

# Initialize the turtle screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
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

# Parameters for the random Koch snowflake
snowflake_order = 5
snowflake_length = 500

# Draw the random Koch snowflake
draw_random_koch_snowflake(koch_turtle, snowflake_order, snowflake_length)

# Keep the window open until clicked
screen.exitonclick()
