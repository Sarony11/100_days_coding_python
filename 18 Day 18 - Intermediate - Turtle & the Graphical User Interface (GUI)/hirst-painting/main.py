"""Create a hirst paiting style using colorgram library"""
from turtle import Turtle, Screen
import random
import colorgram

# Extract 6 colors from an image.
COLOR_VARIETY = 30
colors = colorgram.extract('hirst-painting.webp', COLOR_VARIETY)

def create_RGB_color_palette(color_palette):
    rgb_palette = []
    for c in color_palette:
        r = c.rgb.r
        g = c.rgb.g
        b = c.rgb.b
        rgb_palette.append((r,g,b))
    return rgb_palette

def random_color(color_palette):
    """Return a random color in RGB from a list"""
    return random.choice(color_palette)

def draw_painting():
    for i in range(20):
        for j in range(20):
            o.pencolor(random_color(painting_rgb_palette))
            o.dot(dot_size)
            o.forward(dot_size + dot_spacing_x)
        o.backward(dot_size * 20 + dot_spacing_x * 20)
        o.right(90)
        o.forward(dot_size + dot_spacing_y)
        o.left(90)
    return

# Create the color palette based in the hirst painting
painting_rgb_palette = create_RGB_color_palette(colors)

# Setup turtle
o = Turtle()
Screen().colormode(255)
o.speed(0)
o.seth(0)

# Get the screen dimensions
screen_width = Screen().window_width()
screen_height = Screen().window_height()
print(screen_width,screen_height)

# Calculate the spacing between dots
dot_size = 10
dot_spacing_x = (screen_width - dot_size * 20) / 21  # 20 dots with 21 spacings
dot_spacing_y = (screen_height - dot_size * 20) / 21
print(dot_spacing_x, dot_spacing_y)

# Calculate the position of the top-left dot
x = -screen_width/2 + dot_size/2 + dot_spacing_x/2
y = screen_height/2 - dot_size/2 - dot_spacing_y/2

# Move the turtle to the top-left corner of the screen
o.penup()
o.goto(x, y)

# PAINT!
draw_painting()


Screen().exitonclick()
