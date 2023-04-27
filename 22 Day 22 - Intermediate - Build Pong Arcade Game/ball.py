from turtle import Turtle

class Ball(Turtle):

    def __init__(self,width,height):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("white")
        self.penup()
        self.screen_width = width
        self.screen_height = height
        self.seth(73)
        return
    
    def move_ball(self):
        self.forward(20)
        self.colision_wall()
    
    def colision_wall(self):
        if self.ycor() >= self.screen_height/2:
            if self.seth() >= 270 or self.seth() <= 90:
                self.seth(self.heading()+90)
            else:
                self.seth(self.heading()-90)