# Marquez, Francis Ivan B.,_BSCpE 1-5
# Import
from tkinter import *
from ClassCalculator import *

# Add Window and specifications
window = Tk()
window.geometry("450x600")
window.title("Two Numbers Calculator")
calculator_icon = PhotoImage(file='CalculatorIcon.png')
window.iconphoto(True,calculator_icon)
window.config(background="SeaGreen1")
# Title Box
title_box = Label(window, text="Two Numbers Calculator", font=("Calibri",29,"bold"),fg="white",bg="deep sky blue",
                  relief=RAISED, bd=15,padx=12,pady=15)
title_box.pack()

# Add first number box
first_number_box = Entry(window, font=("Calibri",15))
first_number_box.pack()
# Add second number box
# Buttons for operation
    # Addition
    # Subtraction
    # Multiplication
    # Division
# Output Message

window.mainloop()