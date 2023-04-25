"""Create a hirst paiting style using colorgram library"""
from turtle import Turtle, Screen
import random
import colorgram

# Extract 6 colors from an image.
COLOR_VARIETY = 24
colors = colorgram.extract('hirst-painting.webp', COLOR_VARIETY)

o = Turtle()
Screen().colormode(255)

def create_RGB_color_palette(palette):
    rgb_palette = []
    for c in palette:
        r = c.rgb.r
        g = c.rgb.g
        b = c.rgb.b
        rgb_palette.append((r,g,b))
    return rgb_palette

def random_color():
    """Return a random color in RGB"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    print(r,g,b)
    return (r,g,b)

# Create the color palette based in the hirst painting
painting_rgb_palette = create_RGB_color_palette(colors)




Screen().exitonclick()
