from turtle import Turtle

class Screenboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0,280)
        self.write(f"Score: {self.points}", align="center", move=False, font=("Arial", 12, "normal"))
        return
        
    def score(self):
        self.points += 1
        self.clear()
        self.write(f"Score: {self.points}", align="center", move=False, font=("Arial", 12, "normal"))
        return
    
    def end_game(self):
        self.setpos(0,260)
        self.write(f"Game Over - Your score is {self.points}", align="center", move=False, font=("Arial", 12, "bold"))