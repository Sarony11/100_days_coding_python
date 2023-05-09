from turtle import Turtle
import random

COLORS = ["black","yellow","blue","orange","grey"]

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(1,2)
        self.penup()
        self.seth(180)
        self.goto(300,random.randint(-280,280))