from tkinter import *

window = Tk()
window.minsize(width=300, height=75)
window.config(padx="20",pady="20")

# Define conversion function
def miles_km_conversion():
    km = float(miles_entry.get()) * 1.609344
    km_conversion_label.config(text=km)
    return None

# Define the window title
window.title("Mile to KM converter")

# Define miles section
miles_entry = Entry()
miles_entry.grid(column="1", row="1")

miles_label = Label(text="Miles", font=("Arial",14))
miles_label.grid(column="2", row="1")

# Define KM conversion
is_equal_to_label = Label(text="is equal to", font=("Arial",14))
is_equal_to_label.grid(column="0", row="2")

km_conversion_label = Label(text="0", font=("Arial",14))
km_conversion_label.grid(column="1", row="2")

km_label = Label(text="KM", font=("Arial",14))
km_label.grid(column="2", row="2")

# Define function and button to start the conversion
conversion_button = Button(text="Calculate", command=miles_km_conversion)
conversion_button.grid(column="1", row="3")


window.mainloop()