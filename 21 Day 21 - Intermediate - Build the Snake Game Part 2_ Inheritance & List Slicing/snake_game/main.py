from turtle import Screen
import time
from snake import Snake
from food import Food
from screenboard import Screenboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
game_on = True

s = Screen()
s.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0,0)
screenboard = Screenboard()

snake = Snake()
food = Food()
s.listen()
s.onkey(fun=snake.move_up, key="w")
s.onkey(fun=snake.move_down, key="s")
s.onkey(fun=snake.move_right, key="d")
s.onkey(fun=snake.move_left, key="a")

while game_on:
    s.update()
    time.sleep(0.1)
    # Keep moving the snake all the time
    snake.forward()
    # Detect collision with food
    if snake.check_eat(food):
        screenboard.score()
        food.refresh()
        snake.grow()
    if snake.hit_wall():
        screenboard.end_game() 
        game_on = False
        print("End the Game")
    if snake.hit_tail(): 
        screenboard.end_game()
        game_on = False
        print("End the Game")


s.exitonclick()