from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("high_score.txt",mode="r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            with open("high_score.txt",mode="w") as file:
                file.write("0")
            self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = str(self.score)
            with open("high_score.txt",mode="w") as file:
                file.write(self.high_score)
        self.score = 0
    
    """ def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT) """

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
