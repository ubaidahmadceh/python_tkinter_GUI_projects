from tkinter import *
from random import randint

root = Tk()
root.geometry("400x400")
root.title("Dice Rolling GUI")

heading_label = Label(root, text="This is a Dice Rolling Simulator")
heading_label.pack()

def  roll_function():
    dice_number = randint(1, 6)
    dice_number_label = Label(root, text=dice_number)
    dice_number_label.pack()


submit_button = Button(root, text="Roll a Dice", command=roll_function)
submit_button.pack()

root.mainloop()