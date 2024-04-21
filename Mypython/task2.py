import turtle
tr = turtle.Turtle()
tr.pensize(5)
# Define functions for each color
def blue():
    return "Blue"

def yellow():
    return "Yellow"

def black():
    return "Black"

def green():
    return "Green"

def red():
    return "Red"

# Define a function to print all colors individually
def print_all_colors():
    print("All Colors:")
    print(blue())
    print(yellow())
    print(black())
    print(green())
    print(red())

# Print each color individually
print("Individual Colors:")
print("Blue:", blue())
print("Yellow:", yellow())
print("Black:", black())
print("Green:", green())
print("Red:", red())

# Print all colors at once
print_all_colors()
