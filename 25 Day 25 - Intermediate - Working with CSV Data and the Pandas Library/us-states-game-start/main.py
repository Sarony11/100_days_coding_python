import turtle

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US STATE GAME")
screen.addshape(image)

t = turtle.Turtle()
t.shape(image)

# Define a function to get the mouse coordinates
def get_mouse_click(x, y):
    print("Mouse clicked at x =", x, ", y =", y)

# Call the onscreenclick method and pass the function as argument
turtle.onscreenclick(get_mouse_click)

turtle.mainloop()
#screen.exitonclick()