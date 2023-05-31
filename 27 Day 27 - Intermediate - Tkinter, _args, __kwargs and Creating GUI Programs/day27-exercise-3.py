#import tkinter
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Labels
my_label = Label(text="I am a label", font=("Arial",24,"bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New text")

#Button

def button_clicked():
    my_label.config(text="I was clicked")

# This function updates the text label with the text in my_entry box.
def label_text_on_entry():
    my_label.config(text=my_entry.get())

# I reference this button to the function button_clicked
button = Button(text="Click Me", command=label_text_on_entry)
button.pack()

# Entry
my_entry = Entry(width=10)
my_entry.pack()


window.mainloop()

