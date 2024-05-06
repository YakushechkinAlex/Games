from tkinter import *
from random import *

root = Tk()
root.title('Камень, ножницы, бумага')
root.geometry('600x400')
root.resizable(width=False, height=False)
root['bg'] = 'black'

def whyknb(choice):
    knb = ['Камень', 'Ножницы', 'Бумага']
    computer_choice = choice(knb)
    player_choice = choice

    if player_choice == computer_choice:
        result = "Ничья!"
    elif (player_choice == "Камень" and computer_choice == "Ножницы") or \
         (player_choice == "Ножницы" and computer_choice == "Бумага") or \
         (player_choice == "Бумага" and computer_choice == "Камень"):
        result = "Вы выиграли!"
    else:
        result = "Вы проиграли!"

    labeltext.config(text=f"Вы выбрали: {player_choice}\nКомпьютер выбрал: {computer_choice}\n{result}")

def stone():
    whyknb('Камень')

def scissors():
    whyknb('Ножницы')

def paper():
    whyknb('Бумага')



labeltext = Label(root,text = '', fg = 'white', font = ('Comic Sans MS', 20), bg = 'black')
labeltext.place(y = 200, x = 240)

stone = Button(root, text = 'Камень',
               font = ('Comic Sans MS', 20),
               bg = 'white',
               command = stone)
stone.place(x=50,y=300)

scissors = Button(root, text = 'Ножницы',
               font = ('Comic Sans MS', 20),
               bg = 'white',
               command = scissors)
scissors.place(x=220,y=300)

paper = Button(root, text = 'Бумага',
               font = ('Comic Sans MS', 20),
               bg = 'white',
               command = paper)
paper.place(x=420,y=300)



root.mainloop()