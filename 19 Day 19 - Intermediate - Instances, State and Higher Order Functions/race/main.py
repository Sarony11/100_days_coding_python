from turtle import Turtle, Screen
import random

color_list = ["red", "yellow", "green", "black", "blue",]
picked_colors = []
MOVEMENT = 5
TURTLES = 5
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

s = Screen()
s.setup(SCREEN_WIDTH,SCREEN_HEIGHT)

def random_unique_color(colors):
    color = "red"
    while color in picked_colors:
        color = random.choice(colors)
    picked_colors.append(color)
    return color

def create_turtles(number_turtles, colors):
    turtles = []
    pos_x = (-SCREEN_WIDTH/2)+20
    pos_y = (-SCREEN_HEIGHT/TURTLES)
    if number_turtles > len(color_list):
        print("There are not enough colors for the turtles. Please setup less turtles for the race")
        return False
    for i in range(number_turtles):
        t = Turtle()
        t.penup()
        t.shape("turtle")
        t.color(random_unique_color(colors))
        print(t.color())
        t.setpos(pos_x,pos_y)
        pos_y += SCREEN_HEIGHT/TURTLES/2
        turtles.append(t)
    return turtles

def pick_winner():
    a = s.textinput("Choose a color", "Are you able to guess the color of the winner?: ")
    return a.lower()

def race(turtles,guess):
    on_race = True
    while on_race:
        t = random.choice(turtles)
        t.forward(5)
        pos = t.pos()
        if pos[0] >= SCREEN_WIDTH/2:
            return t

def check_winer(t):
    if guess != t.color()[0]:
        print("You loose... Try again!")
        return False
    else:
        print("Great! You have been able to guess the color! You have super powers!")
        return True

turtles = create_turtles(TURTLES,color_list)
guess = pick_winner()
check_winer(race(turtles,guess))

s.exitonclick()