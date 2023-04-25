from turtle import Turtle, Screen

t = Turtle()
s = Screen()
s.listen()

def forward():
    t.forward(5)
    return

def turn_right():
    t.right(5)
    return

def turn_left():
    t.left(5)
    return

s.onkey(key="space", fun=forward)
s.onkey(key="Right", fun=turn_right)
s.onkey(key="Left", fun=turn_left)

s.exitonclick()