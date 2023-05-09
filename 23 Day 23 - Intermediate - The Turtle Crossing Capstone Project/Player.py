from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.shapesize(2,2)
        self.penup()
        self.seth(90)
        self.goto(0,-280)

    def move_up(self):
        self.forward(5)

    def move_left(self):
        xcor = self.xcor() - 5
        self.goto(xcor,self.ycor())

    def move_right(self):
        xcor = self.xcor() + 5
        self.goto(xcor,self.ycor())