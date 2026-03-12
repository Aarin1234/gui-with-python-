import tkinter
from tkinter import*
import tkinter.messagebox
import random

root = Tk()
root.title('Jumbled Word Game')


#Creating the lists for the game
answers = ['apple', 'mango', 'kiwi', 'phone', 'room', 'water',
            'food','original']

words = ['plape', 'goman', 'wiki','ehopn','moro', 'tawer',
            'dofo','niliroga']

num = random.randrange(0,len(words),1)
#c = correct ans count
c = 0
#total num of question
d = 0
#score string to display
s = ''
#Label widget to display the score
l = Label(root)


#GUI
root.geometry('700x500+500+150')
root.configure(bg= 'black')
Label(root, text='Lets play jumbled word game!', font=('Verdana',28),
       fg='yellow', bg='black').pack(pady=5)
label = Label(root, font=('Verdana', 20), fg='blue', bg='black')
label.pack(pady=30)



root.mainloop()
