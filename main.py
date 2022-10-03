import random
import time
from tkinter import *

def win (n):
    global game
    if (game[0] == n and game[1] == n and game[2] == n) or (game[3] == n and game[4] == n and game[5] == n) or (game[6] == n and game[7] == n and game[8]== n) or \
        (game[0] == n and game[3] == n and game[6] == n) or (game[1] == n and game[4] == n and game[7] == n) or (game[2] == n and game[5] == n and game[8]== n) or \
        (game[0] == n and game[4] == n and game[8] == n) or (game[2] == n and game[4] == n and game[6] == n):
        return True

def push(b):
    global game
    global game_left
    global turn

    game[b] = 'X'
    buttons[b].config(text='X', bg='white', state='disabled')
    game_left.remove(b)

    t = random.choice(game_left)
    if game[t] != 'X':
        game[t] = '0'
        time.sleep(0.5)
        buttons[t].config(text='0', bg='white', state='disabled')
        if win('X'):
            window = Tk()
            window.title("Вы победили!")
            lbl = Label(window, text="Поздравляю!", bg ='yellow', font=("Arial Bold", 50))
            lbl.grid(column=0, row=0)
            window.mainloop()
        elif win('0'):
            window = Tk()
            window.title("Вы проиграли!")
            lbl = Label(window, text="Победил искусственный интеллект!", bg='blue', font=("Arial Bold", 50))
            lbl.grid(column=0, row=0)
            window.mainloop()
        else:
            if (len(game_left) > 1):
                game_left.remove(t)
            else:
                turn += 1
    else:
        t = random.choice(game_left)

game = [None] * 9
game_left = list(range(9))
turn = 0

root = Tk()
root.title('Крестики-нолики')
lbl = Label(root, text="Игра началась!")
lbl.grid(column=0, row=0)


buttons = [Button(width=5, height=2, font=('Arial', 20, 'bold'), bg='pink', command=lambda x=i: push(x)) for i in
           range(9)]

myLabel = Label()
myLabel.grid(row=0, column=0, columnspan=3)
row = 1
col = 0
for i in range(9):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0

root.mainloop()