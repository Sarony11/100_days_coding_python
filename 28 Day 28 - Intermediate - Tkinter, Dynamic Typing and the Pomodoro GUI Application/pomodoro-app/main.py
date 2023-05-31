from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
# https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 25*60
SHORT_BREAK_SEC = 5*60
LONG_BREAK_SEC = 20*60
times = 0
marks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    global times
    global timer
    global marks
    times = 0
    marks = ""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="TIMER", font=(FONT_NAME,50,"bold"), foreground=GREEN, background=YELLOW)
    timer_check_label.config(text=marks, font=(FONT_NAME,25,"bold"), foreground=GREEN, background=YELLOW)
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global times
    global marks
    times += 1

    if times % 8 == 0:
        count_down(LONG_BREAK_SEC)
        timer_label.config(text="Long Break", font=(FONT_NAME,50,"bold"), foreground=RED, background=YELLOW)
    elif times % 2 == 0:
        count_down(SHORT_BREAK_SEC)
        timer_label.config(text="Short Break", font=(FONT_NAME,50,"bold"), foreground=RED, background=YELLOW)
    else:
        marks += "✔"
        count_down(WORK_SEC)
        timer_label.config(text="WORK", font=(FONT_NAME,50,"bold"), foreground=GREEN, background=YELLOW)
        timer_check_label.config(text=marks, font=(FONT_NAME,25,"bold"), foreground=GREEN, background=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    if count >= 0:
        count_min, count_sec = divmod(count,60)
        canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

""" def count_down(time_left):
    count_min, count_sec = divmod(time_left,60)
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if time_left > 0:
        window.after(1000,count_down,time_left-1) """

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,background=YELLOW)

# Define the canva for the tomato image
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="resources/tomato.png")
canvas.create_image(102,112,image=tomato_img)
timer_text = canvas.create_text(102,130,text="00:00",fill="white",font=(FONT_NAME,25,"bold"))
canvas.grid(column=1,row=1)

timer_label = Label(text="TIMER", font=(FONT_NAME,50,"bold"), foreground=GREEN, background=YELLOW)
timer_label.grid(column=1,row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", command=reset_time)
reset_button.grid(column=2,row=2)

timer_check_label = Label(text="", font=(FONT_NAME,25,"bold"), foreground=GREEN, background=YELLOW)
timer_check_label.grid(column=1,row=3)

window.mainloop()