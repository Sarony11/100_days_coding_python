from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.shapesize(1,1)
        self.penup()
        self.seth(90)
        self.goto(0,-280)
        self.player_speed = 0.1
        self.races = 0

    def move_up(self):
        self.forward(5)

    def reset(self):
        self.player_speed *= 0.9
        self.races += 1
        self.goto(0,-280)