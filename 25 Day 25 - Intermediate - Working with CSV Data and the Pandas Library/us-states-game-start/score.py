from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        return

    def write_state(self,state_name,state_coordinates):
        self.goto(state_coordinates)
        self.write(f"{state_name}", align="center", move=False, font=("Arial", 12, "normal"))

    def score(self):
        self.points += 1
        return
    
    def game_over(self):
        self.setpos(0,260)
        self.write(f"Game Over - Your score is {self.points}", align="center", move=False, font=("Arial", 18, "bold"))