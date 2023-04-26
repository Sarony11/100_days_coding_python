from turtle import Turtle, Screen
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
game_on = True

s = Screen()
s.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0,0)
#t = Turtle()

def init_snake():
    snake = []
    pos = 0
    for i in range(3):
        snake.append(Turtle("square"))
        snake[i].color("white")
        snake[i].penup()
        snake[i].backward(pos)
        pos += 20
    s.update()
    return snake

def move(snake):
    for i in range(len(snake) -1, -1, -1):
        snake[i].forward(20)
        if snake[i].heading() != snake[i-1].heading():
            snake[i].seth() == snake[i-1].heading()
    s.update()
    time.sleep(0.05)
    return

def move_up():
    snake[0].seth(90)
    return

def move_down():
    snake[0].seth(270)
    return

def move_right():
    snake[0].seth(0)
    return

def move_left():
    snake[0].seth(180)
    return

snake = init_snake()
while game_on:
    move(snake)


s.exitonclick()