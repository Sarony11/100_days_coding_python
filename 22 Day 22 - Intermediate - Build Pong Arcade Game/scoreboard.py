from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self,width,height):
        super().__init__()
        self.points = 0
        self.color("white")
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.setpos(-(width/2)*0.1,(height/2)*0.8)
        self.write(f"{self.points}", align="center", move=False, font=("Arial", 18, "normal"))
        return
        
    def score(self):
        self.points += 1
        self.clear()
        self.write(f"{self.points}", align="center", move=False, font=("Arial", 18, "normal"))
        return