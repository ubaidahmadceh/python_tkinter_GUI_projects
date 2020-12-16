from tkinter import *
from random import randint
root = Tk()
root.title("Number Guessing Game GUI")
root.geometry('600x600')

global health 
health = 10

def age_function():
    age_label = Label(root, text="Hi, "+name.get()+" What's your age?")
    age_label.pack()
    global age
    age = Entry(root)
    age.pack()
    age_submit_button = Button(root, text="Submit", command=game_start_0_function)
    age_submit_button.pack()

def game_start_0_function():
    age_integer = int(age.get())
    if age_integer >= 18:
        welcome_label = Label(root, text="You are eligible to play the game")
        welcome_label.pack()
        play_game_button = Button(root, text="Play", command=game_start_1_function)
        play_game_button.pack()
        
    else:
        cant_play_label = Label(root, text="Sorry you have to wait till you turn 18")
        cant_play_label.pack()

def game_start_1_function():
    game_line_1 = Label(root, text="Road is dividing into left and right")
    game_line_1.pack()
    game_line_2 = Label(root, text="Which path you will chose?")
    game_line_2.pack()
    game_line_3 = Label(root, text="left")
    game_line_3.pack()
    game_line_4 = Label(root, text="right")
    game_line_4.pack()
    global user_decision_1
    user_decision_1 = Entry(root)
    user_decision_1.pack()
    decision_1_submit_button = Button(root, text="Submit", command=game_start_2_function)
    decision_1_submit_button.pack()



def game_start_2_function():
    if user_decision_1.get() == "left":
        game_line_5 = Label(root, text="Now there is a house and a strange pond , So what will you chose? house or pond")
        game_line_5.pack()
        global user_decision_1_2
        user_decision_1_2 = Entry(root)
        user_decision_1_2.pack()
        user_decision_1_2_submit = Button(root, text="Submit", command=game_start_3_function)
        user_decision_1_2_submit.pack()


def game_start_3_function():
    if user_decision_1_2.get() == "house":
        game_line_6 = Label(root, text="you had a fight with them and you lose your health. Write health to find out your new health")
        game_line_6.pack()
        global new_health
        new_health = health - 5
        global find_out_health
        find_out_health = Entry(root)
        find_out_health.pack()
        find_out_health_submit = Button(root, text="Submit", command=game_start_4_function)
        find_out_health_submit.pack()

    elif user_decision_1_2.get() == "pond":
        game_line_7 = Label(root, text="you have a happy life now. you live by fishing Write thankyou to me for saving you")
        game_line_7.pack()
        global thnx
        thnx = Entry(root)
        thnx.pack()
        thnx_submit=Button(root, text="Submit",command=game_start_5_function)
        thnx_submit.pack()


def game_start_4_function():
    if find_out_health.get() == "health":
        find_out_health_label = Label(root, text=new_health)
        find_out_health_label.pack()

def game_start_5_function():
    if thnx.get() == "thankyou":
        thnx_label_1 = Label(root, text="your welcome")
        thnx_label_1.pack()

name_label = Label(root, text="Enter your Name")
name_label.pack()
name = Entry(root)
name.pack()
name_submit_button = Button(root, text="Submit", command=age_function)
name_submit_button.pack()

root.mainloop()
