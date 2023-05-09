from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-250,250)
        self.write(f"{self.points}", align="center", move=False, font=("Arial", 18, "normal"))
        return
        
    def score(self,plus):
        self.points += plus
        self.clear()
        self.write(f"{self.points}", align="center", move=False, font=("Arial", 18, "normal"))
        return
    
    def game_over(self):
        self.setpos(0,260)
        self.write(f"Game Over - Your score is {self.points}", align="center", move=False, font=("Arial", 18, "bold"))