from turtle import Screen, Turtle
import time
from Player import Player
from Car import Car
from CarManager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
game_on = True

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("white")
screen.title("Turtle Racing")
screen.tracer(0,0)

player = Player()
score_board = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up,key="w")

while game_on:
    time.sleep(player.player_speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_all()
    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            score_board.game_over()
            game_on = False
    if player.ycor() >= 300:
        player.reset()
        score_board.score(player.races)

screen.exitonclick()