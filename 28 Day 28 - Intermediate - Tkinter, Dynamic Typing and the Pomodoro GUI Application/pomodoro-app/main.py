from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
# https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    return

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,background=YELLOW)

# Define the canva for the tomato image
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="resources/tomato.png")
canvas.create_image(102,112,image=tomato_img)
canvas.create_text(102,130,text="00:00",fill="white",font=(FONT_NAME,25,"bold"))
canvas.grid(column=1,row=1)

timer_label = Label(text="TIMER", font=(FONT_NAME,50,"bold"), foreground=GREEN, background=YELLOW)
timer_label.grid(column=1,row=0)

start_button = Button(text="Start", command=reset_time)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", command=reset_time)
reset_button.grid(column=2,row=2)

timer_check_label = Label(text="✔", font=(FONT_NAME,25,"bold"), foreground=GREEN, background=YELLOW)
timer_check_label.grid(column=1,row=3)

window.mainloop()