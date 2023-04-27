from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,height):
        super().__init__()
        self.paddle = []
        self.create_paddle(height)
        return
    
    def create_paddle(self,height):
        pos = 20
        for n in range(3):
            part = Turtle("square")
            part.color("white")
            part.penup()
            part.setpos((-height/2 + (height/20)),pos)
            self.paddle.append(part)
            pos -= 20
        return
        
    def move_up(self):
        for part in self.paddle:
            part.seth(90)
            part.forward(20)
        return

    def move_down(self):
        for part in self.paddle[::-1]:
            part.seth(270)
            part.forward(20)
        return
