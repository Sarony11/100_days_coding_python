from turtle import Screen
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
game_on = True

s = Screen()
s.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0,0)


while game_on:
    s.update()
    time.sleep(0.1)



s.exitonclick()