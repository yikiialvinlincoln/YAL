import turtle
tr = turtle.Turtle()
tr.pensize(5)

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

def all_colors():
    colors = [blue(), yellow(), black(), green(), red()]
    return colors

# Test the functions
print("Blue:", blue())
print("Yellow:", yellow())
print("Black:", black())
print("Green:", green())
print("Red:", red())
print("All Colors:", all_colors())
