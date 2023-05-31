# Import tkinter library
import tkinter

# Define the tkinter object
window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(500,300)

my_label = tkinter.Label(text="I am a label",font=("Arial",26,"bold"))
my_label.pack(side="left",expand=True)

# Method to keep the window open
window.mainloop()
