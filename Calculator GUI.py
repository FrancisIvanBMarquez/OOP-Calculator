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
title_box = Label(window, text="Two Numbers Calculator")
title_box.pack()

# Add first number box
# Add second number box
# Buttons for operation
    # Addition
    # Subtraction
    # Multiplication
    # Division
# Output Message

window.mainloop()