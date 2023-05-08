from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self,width,height):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("white")
        self.penup()
        self.screen_width = width
        self.screen_height = height
        return
    
    def move_ball(self):
        xcor = self.xcor()+2
        ycor = self.ycor()+2
        self.setpos(xcor,ycor)
        self.colision_wall()
    
    def colision_wall(self):
        if self.ycor() >= (self.screen_height/2)-20:
            if (self.heading() > 270 or self.heading() > 90):
                self.seth(self.heading()+90)
            else:
                self.seth(self.heading()-90)
        if self.ycor() <= (-self.screen_height/2)+20:
            if (self.heading() > 270 or self.heading() > 90):
                self.seth(self.heading()-90)
            else:
                self.seth(self.heading()+90)
