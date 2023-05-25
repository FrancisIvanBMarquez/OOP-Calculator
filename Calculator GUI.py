# Marquez, Francis Ivan B.,_BSCpE 1-5
# Import
from tkinter import *
from ClassCalculator import *

# Add Window and specifications
window = Tk()
window.geometry("450x700")
window.title("Two Numbers Calculator")
calculator_icon = PhotoImage(file='CalculatorIcon.png')
window.iconphoto(True,calculator_icon)
window.config(background="SeaGreen1")

# Title Box
title_box = Label(window, text="Two Numbers Calculator", font=("Calibri",29,"bold"),fg="white",bg="deep sky blue",
                  relief=RAISED, bd=15,padx=12,pady=15)
title_box.pack()

# Add first number box
first_number_box = Entry(window, font=("Calibri",15),bd=5)
first_number_box.place(x=120,y=150)
# Add second number box
second_number_box = Entry(window, font=("Calibri",15),bd=5)
second_number_box.place(x=120, y=200)

# Buttons for operation
# images for icons
add_icon = PhotoImage(file="add icon.png")
subtract_icon = PhotoImage(file="subtract icon.png")
multiply_icon = PhotoImage(file="multiply icon.png")
divide_icon = PhotoImage(file="divide icon.png")

    # Addition
addition_button = Button(window, text="Add",font=("Calibri",25),fg="white",bg="deep sky blue",
                         activeforeground="white",activebackground="deep sky blue",image=add_icon,compound="bottom")
addition_button.place(x=100,y=250)
     # Subtraction
subtraction_button = Button(window, text="Subtract",font=("Calibri",25),fg="white",bg="deep sky blue",
                         activeforeground="white",activebackground="deep sky blue",image=subtract_icon,compound="bottom")
subtraction_button.place(x=100,y=450)
    # Multiplication
multiplication_button = Button(window, text="Multiply",font=("Calibri",25),fg="white",bg="deep sky blue",
                         activeforeground="white",activebackground="deep sky blue",image=multiply_icon,compound="bottom")
multiplication_button.place(x=300,y=250)
    # Division
division_button = Button(window, text="Divide",font=("Calibri",25),fg="white",bg="deep sky blue",
                         activeforeground="white",activebackground="deep sky blue",image=divide_icon,compound="bottom")
division_button.place(x=300,y=450)

# Output Message

window.mainloop()