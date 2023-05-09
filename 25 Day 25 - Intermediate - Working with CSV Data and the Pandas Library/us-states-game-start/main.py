import turtle
import pandas
from score import Score

image = "blank_states_img.gif"
states_df = pandas.read_csv("50_states.csv")
state_list = list(states_df.state)
state_count = len(state_list)
print(state_list)

screen = turtle.Screen()
screen.title("US STATE GAME")
screen.addshape(image)
turtle.shape(image)

# Get the width and height of the image map
width = 725
height = 491
print(width,height)

# Set the screen size to match the image map
screen.setup(width, height)

score = Score()

while len(state_list) < 50:
    answer_state = screen.textinput(title=f"({score.points}/{state_count}) Guess State", prompt="What's another state's name?:")
    if state_list.count(answer_state) == 1:
        state_list.remove(answer_state)
        state = states_df[states_df.state == answer_state]
        state_coordinates = (int(state.x),int(state.y))
        score.write_state(answer_state, state_coordinates)
        score.score()

""" # Define a function to get the mouse coordinates
def get_mouse_click(x, y):
    print("Mouse clicked at x =", x, ", y =", y)

# Call the onscreenclick method and pass the function as argument
turtle.onscreenclick(get_mouse_click) """

turtle.mainloop()
#screen.exitonclick()