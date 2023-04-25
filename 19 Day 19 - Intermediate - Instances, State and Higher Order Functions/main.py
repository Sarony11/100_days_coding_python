from turtle import Turtle, Screen

MOVEMENT = 5

t = Turtle()
s = Screen()
s.listen()

def forward():
    t.forward(MOVEMENT)
    return

def backward():
    t.backward(MOVEMENT)
    return

def turn_right():
    t.right(MOVEMENT)
    return

def turn_left():
    t.left(MOVEMENT)
    return

def clear():
    t.setpos(0,0)
    t.clear()

s.onkey(key="w", fun=forward)
s.onkey(key="s", fun=backward)
s.onkey(key="d", fun=turn_right)
s.onkey(key="a", fun=turn_left)
s.onkey(key="space", fun=clear)

s.exitonclick()