import time
import pyautogui
from tkinter import *

def take_screenshot():
    time.sleep(5)
    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)
    image = pyautogui.screenshot(name)
    
root = Tk()
root.geometry("400x400")
root.title("Screenshot APP")

ss_button = Button(root, text="Take Screenshot", command=take_screenshot)
ss_button.pack()

close_button = Button(root, text="Quit", command=quit)
close_button.pack()

root.mainloop()

# pip install pyautogui
# pip install pillow