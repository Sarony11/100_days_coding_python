from turtle import Turtle, Screen

o = Turtle()
sides = 4
angle = 360/sides

o = Turtle()
o.speed(0)
sides = 8
angle = 360/sides

for _ in range(sides):
    for _ in range(10):
        o.forward(3)
        o.pd()
        o.forward(3)
        o.pu()     
    o.right(angle)

screen = Screen()
screen.exitonclick()