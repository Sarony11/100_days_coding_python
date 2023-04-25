"""Make a spirograph tha changes the color randomly"""
from turtle import Turtle, Screen
import random

direction = [0, 90, 180, 270]

o = Turtle()
o.speed(0)
o.pensize(1)
Screen().colormode(255)

ANGLE = 5
current_direction = None
new_direction = None
o.setheading(0)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    print(r,g,b)
    return (r,g,b)

def draw_spirograph():
    for _ in range(int(360/ANGLE)):
        o.pencolor(random_color())
        o.right(ANGLE)
        o.circle(80)
    return

draw_spirograph()   

Screen().exitonclick()
