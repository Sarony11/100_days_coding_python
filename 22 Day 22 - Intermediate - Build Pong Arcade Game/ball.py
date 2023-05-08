from turtle import Turtle

class Ball(Turtle):

    def __init__(self,width,height):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("white")
        self.penup()
        self.screen_width = width
        self.top_wall = (height/2)-height/40
        self.bottom_wall = -(height/2)+height/40
        self.screen_height = height
        self.xmove = 10
        self.ymove = 10
        return
    
    def move_ball(self):
        xcor = self.xcor() + self.xmove
        ycor = self.ycor() + self.ymove
        self.setpos(xcor,ycor)
        self.colision_wall()
    
    def colision_wall(self):
        if self.ycor() >=  self.top_wall or self.ycor() <= self.bottom_wall:
            self.ymove *= -1