from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,width,height):
        super().__init__()
        self.shape("square")
        self.shapesize(1,5,None)
        self.color("white")
        self.penup()
        self.screen_width = width
        self.screen_height = height
        self.setpos(-(width/2)+(width*0.1), 0)
        self.seth(90)
        return
        
    def move_up(self):
        if self.ycor() < (self.screen_height/2)-(self.screen_height*0.1):
            self.forward(20)
            return

    def move_down(self):
        if self.ycor() > (-self.screen_height/2)+(self.screen_height*0.1):
            self.backward(20)
            return
