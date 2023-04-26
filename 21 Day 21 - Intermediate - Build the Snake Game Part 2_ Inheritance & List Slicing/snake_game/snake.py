from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        return

    def grow(self):
        part = Turtle("square")
        part.color("white")
        part.penup()
        part.setpos(self.snake[-1].pos())
        part.backward(20)
        self.snake.append(part)


    def create_snake(self):
        for n in range(3):
            if len(self.snake) == 0:
                part = Turtle("square")
                part.color("white")
                part.penup()
                part.setpos(0,0)
                self.snake.append(part)
            else:
                self.grow()
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
        if self.snake[0].heading() != 360-90:
            self.snake[0].seth(90)
        return

    def move_down(self):
        if self.snake[0].heading() != 360-270:
            self.snake[0].seth(270)
        return

    def move_right(self):
        if self.snake[0].heading() != 360-0:
            self.snake[0].seth(0)
        return

    def move_left(self):
        if self.snake[0].heading() != 360-180:
            self.snake[0].seth(180)
        return
    
    def hit_wall(self):
        if self.snake[0].xcor() == -300 or self.snake[0].ycor() == -300 or self.snake[0].xcor() == 300 or self.snake[0].ycor() == 300:
            return True
        else:
            return False