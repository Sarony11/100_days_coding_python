from turtle import Turtle, Screen
import time
from snake import Snake

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
game_on = True

s = Screen()
s.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0,0)

snake = Snake()
s.listen()
s.onkey(fun=snake.move_up, key="w")
s.onkey(fun=snake.move_down, key="s")
s.onkey(fun=snake.move_right, key="d")
s.onkey(fun=snake.move_left, key="a")

while game_on:
    s.update()
    time.sleep(0.5)
    snake.forward()


s.exitonclick()