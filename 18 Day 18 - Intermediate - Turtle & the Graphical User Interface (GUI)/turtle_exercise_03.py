"""Make random lines picking a real random color"""
from turtle import Turtle, Screen
import random

direction = [0, 90, 180, 270]

o = Turtle()
o.speed(5)
o.pensize(5)
Screen().colormode(255)

current_direction = None
new_direction = None

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    print(r,g,b)
    return (r,g,b)

def random_direction():
    new_direction = random.choice(direction)
    if new_direction != current_direction:
        o.setheading(new_direction)
        new_direction = current_direction
    return

for _ in range(10000):
    while True:
        random_direction()        
        o.pencolor(random_color())
        o.fd(20)

Screen().exitonclick()
