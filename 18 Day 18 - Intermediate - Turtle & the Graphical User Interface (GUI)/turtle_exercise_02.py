"""Make random lines picking a color in each section"""
from turtle import Turtle, Screen
import random

color = ["CornflowerBlue", "DarkOrchid", "BlanchedAlmond", "DeepSkyBlue", "GreenYellow", "HotPink", "IndianRed", "LawnGreen", "LightGray"]
direction = [0, 90, 180, 270]

o = Turtle()
o.speed(5)
o.pensize(5)
current_direction = None
new_direction = None

for _ in range(10000):
    while True:
        new_direction = random.choice(direction)
        if new_direction != current_direction:
            o.setheading(new_direction)
            break
    o.color(random.choice(color))
    o.fd(20)

screen = Screen()
screen.exitonclick()