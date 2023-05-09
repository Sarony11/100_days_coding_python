from turtle import Screen, Turtle
import time
from Player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
game_on = True

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("white")
screen.title("Turtle Racing")
screen.tracer(0,0)

player = Player()

screen.listen()
screen.onkey(player.move_up,key="w")
screen.onkey(player.move_left,key="a")
screen.onkey(player.move_right,key="d")

while game_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()