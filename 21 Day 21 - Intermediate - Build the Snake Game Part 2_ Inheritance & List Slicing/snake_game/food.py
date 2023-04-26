from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        return

    def refresh(self):
        self.goto(random.randint(-(600-40)/2,(600-40)/2),random.randint(-(600-40)/2,(600-40)/2))
        return