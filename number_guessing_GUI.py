from tkinter import *
from random import randint
root = Tk()
root.title("Number Guessing wali Game GUI")
root.geometry('300x300')

number = randint(1,11)
def check():
    user_guess_integer = int(user_guess.get())
    if user_guess_integer == number:
        statement_1 = Label(root, text="you win this game")
        statement_1.pack()
    elif user_guess_integer > number:
        statement_2 = Label(root, text="Too large guess")
        statement_2.pack()
    elif user_guess_integer < number:
        statement_3 = Label(root, text="Too small guess")
        statement_3.pack()
    else:
        statement_4 = Label(root, text="Please guess between 0 to 10")
        statement_4.pack()

user_guess = Entry(root)
user_guess.pack()

check_button = Button(root, text="Check", command=check)
check_button.pack()

root.mainloop()