from turtle import Screen
import time
from paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
game_on = True

s = Screen()
s.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
s.bgcolor("black")
s.title("Ping Pong")
s.tracer(0,0)
s.delay(10)
p1 = Paddle(SCREEN_WIDTH,SCREEN_HEIGHT)
p2 = Paddle(-SCREEN_WIDTH,SCREEN_HEIGHT)

s.listen()
s.onkey(lambda: p1.move_up(),key="w")
s.onkey(lambda: p1.move_down(),key="s")
s.onkey(lambda: p2.move_up(),key="i")
s.onkey(lambda: p2.move_down(),key="k")


while game_on:
    s.update()
    time.sleep(0.001)



s.exitonclick()