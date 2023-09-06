# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 13:22:44 2023

@author: User
"""

from tkinter import *
import random

root = Tk()
root.geometry('700x700')
root.resizable(0, 0)
root.title('From DataFlair - Rock, Paper, Scissors game')
root.config(bg = 'silver')

Label(root, text = "You have only 3 tries, After the 3 tries exit then run game to restart", 
      font = 'georgia 15', fg = 'red', 
      bg = 'silver').pack(pady = 5)

Label(root, text = 'Rock, Paper, Scissor', 
      font = 'georgia 20 bold', fg = 'grey',
      bg = 'silver').pack()

user_choice = StringVar()

Label(root, text = "rock, paper, scissor - what's your choice", 
      font = 'georgia 15 bold', 
      bg = 'silver').pack(pady = 30)

Entry(root, font = 'georgia 13', textvariable = user_choice, 
      bg = 'antiquewhite').pack(pady = 50) 

list = ['rock', 'paper', 'scissor']

comp_choice = random.choice(list)
#comp_choice = random.randint(1, 3)
"""if comp_choice == 1:
    comp_choice = 'rock'
elif comp_choice == 2:
    comp_choice = 'paper'
else:
    comp_choice = 'scissor'
"""

result = StringVar()
def play():
    user_input = user_choice.get()
    if user_input == comp_choice:
        result.set("It's a tie")
    elif user_input == 'rock' and comp_choice == 'paper':
        result.set("You lost, computer won")
    elif user_input == 'rock' and comp_choice == 'scissor':
        result.set("You won, computer lost")
    elif user_input == 'paper' and comp_choice == 'scissor':
        result.set("You lost, computer won")
    elif user_input == 'paper' and comp_choice == 'rock':
        result.set("You won, computer lost")
    elif user_input == 'scissor' and comp_choice == 'rock':
        result.set("You lost, computer won")
    elif user_input == 'scissor' and comp_choice == 'paper':
        result.set("You won, computer lost")
    else:
        result.set("Choose either rock, paper or scissor")

def reset():
    result.set("")
    user_choice.set("")
    
def exit():
    root.destroy()
    
Entry(root, font = 'georgia 12 bold', textvariable = result, 
      bg = 'silver', width = 50).pack(pady = 20)
Button(root, font = 'georgia 12 bold', text = 'PLAY', padx = 5, 
       bg = 'silver', command = play).pack(pady = 20)
Button(root, font = 'georgia 12 bold', text = 'RESET', padx = 5, 
       bg = 'silver', command = reset).pack(pady = 20)
Button(root, font = 'georgia 12 bold', text = 'EXIT', padx = 5, 
       bg = 'silver', command = exit).pack(pady = 20)

root.mainloop()

















