from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake(self.snake)
        return

    def create_snake(self,snake):
        pos = 0
        for n in range(3):
            part = Turtle("square")
            part.color("white")
            part.penup()
            part.backward(pos)
            snake.append(part)
            pos += 20
        return

    def forward(self):
        for i in range(len(self.snake) -1, -1, -1):
            self.snake[i].forward(20)
            if self.snake[i].heading() != self.snake[i-1].heading():
                if i != 0:
                    self.snake[i].seth(self.snake[i-1].heading())
        return

    def check_eat(self,food):
        if self.snake[0].distance(food) < 15: 
            return True
        else:
            return False

    def move_up(self):
        self.snake[0].seth(90)
        return

    def move_down(self):
        self.snake[0].seth(270)
        return

    def move_right(self):
        self.snake[0].seth(0)
        return

    def move_left(self):
        self.snake[0].seth(180)
        return