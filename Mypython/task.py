import turtle

# Define functions for each color
def draw_blue():
    turtle.color("blue")
    turtle.circle(50)

def draw_yellow():
    turtle.color("yellow")
    turtle.circle(50)

def draw_black():
    turtle.color("black")
    turtle.circle(50)

def draw_green():
    turtle.color("green")
    turtle.circle(50)

def draw_red():
    turtle.color("red")
    turtle.circle(50)

# Define a function to draw all colors
def draw_all_colors():
    colors = [draw_blue, draw_yellow, draw_black, draw_green, draw_red]
    for color_function in colors:
        color_function()

# Initialize turtle screen
turtle.setup(600, 600)
turtle.speed(1)

# Draw each color individually
draw_blue()
draw_yellow()
draw_black()
draw_green()
draw_red()

# Draw all colors together
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()
draw_all_colors()

# Keep the window open
turtle.done()
