import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import math

# Define the acceleration due to gravity
gravity = 9.81

# Function to initialize the main window
def main():
    root = tk.Tk()
    frm_main = Frame(root)
    frm_main.master.title("Swing time of a pendulum")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    populate_main_window(frm_main)
    root.mainloop()

# Function to populate the main window with labels, entry boxes, and buttons
def populate_main_window(frm_main):
    # Labels and entry box for pendulum length
    lbl_length = Label(frm_main, text="Pendulum Length (L): ")
    ent_length = IntEntry(frm_main, width=3, lower_bound=1, upper_bound=90)
    lbl_length_units = Label(frm_main, text="meters")

    # Labels for period and frequency
    lbl_period_name = Label(frm_main, text="Period:")
    lbl_frequency_name = Label(frm_main, text="Frequency:")

    # Labels to display the calculated period and frequency
    lbl_period_show = Label(frm_main, width=6)  
    lbl_frequency_show = Label(frm_main, width=6)  

    # Labels for units of period and frequency
    lbl_period_units = Label(frm_main, text="seconds")
    lbl_frequency_units = Label(frm_main, text="Hz")  

    # Clear button
    btn_clear = Button(frm_main, text="Clear")

    # Grid layout for widgets in the main window
    lbl_length.grid(row=0, column=0, padx=3, pady=3)
    ent_length.grid(row=0, column=1, padx=3, pady=3, sticky="w")  # Set sticky to "w" to move the entry to the left
    lbl_length_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_period_name.grid(row=1, column=0, padx=(30, 3), pady=3)
    lbl_period_show.grid(row=1, column=1, padx=3, pady=3)  
    lbl_period_units.grid(row=1, column=2, padx=3, pady=3)

    lbl_frequency_name.grid(row=1, column=3, padx=(30, 3), pady=3)  
    lbl_frequency_show.grid(row=1, column=4, padx=3, pady=3)  
    lbl_frequency_units.grid(row=1, column=5, padx=0, pady=3) 

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")

    # Function to calculate period and frequency
    def calculate(event):
        try:
            length = ent_length.get()
            period = 2 * math.pi * math.sqrt(length / gravity)
            frequency = 1 / period

            lbl_period_show.config(text=f"{period:.2f}")
            lbl_frequency_show.config(text=f"{frequency:.2f}")

        except ValueError:
            lbl_period_show.config(text="")
            lbl_frequency_show.config(text="")

    # Function to clear inputs and outputs
    def clear():
        ent_length.clear()
        lbl_period_show.config(text="")
        lbl_frequency_show.config(text="")
        ent_length.focus()

    # Bind the calculate function to the length entry box so
    # that the computer will call the calculate function
    # when the user releases the key.
    ent_length.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the length entry box.
    ent_length.focus()

# Check if the script is being run directly
if __name__ == "__main__":
    main()