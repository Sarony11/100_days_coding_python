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

    def move_up(self):
        self.forward(5)