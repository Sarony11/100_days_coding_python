from turtle import Screen
import time
from paddle import Paddle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
game_on = True

s = Screen()
s.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0,0)
p1 = Paddle(SCREEN_HEIGHT)
#p2 = Paddle(SCREEN_HEIGHT)

s.listen()
s.onkey(fun=p1.move_up,key="w")
s.onkey(fun=p1.move_down,key="s")


while game_on:
    s.update()
    time.sleep(0.1)



s.exitonclick()