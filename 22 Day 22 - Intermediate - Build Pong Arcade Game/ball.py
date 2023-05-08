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
        self.xmove = 10
        self.ymove = 10
        return
    
    def move_ball(self):
        xcor = self.xcor() + self.xmove
        ycor = self.ycor() + self.ymove
        self.setpos(xcor,ycor)
    
    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
    