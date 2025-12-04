from tkinter import*
import time
from tkinter import messagebox

root = Tk()
root.geometry('300x300')
root.title('Time Countdown')
root.configure(bg='green')
#creating some user deined function
def submit():
    try:
        temp = int(hour.get()) *3600 + int(minute.get()) *60 + int(second.get())
    except:
        print('please input a valid value!')
    while temp>-1:
        mins,secs = divmod(temp, 60)
        hours = 00
        if mins > 60:
            hours,mins = divmod(mins, 60)
    hour.set('{00:2d}'.format(hours))
    minute.set('{00:2d}'.format(minute))
    second.set('{00:2d}'.format(second))

    root.update()
    time.sleep(1)

    if temp == 60:
        messagebox.showinfo('Time Window','Times Up')
    temp -= 1

#creating the variables and entrys
hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set('00')
minute.set('00')
second.set('00')

hour_entry = Entry(root, width = 3,font = ('Arial',21,''), textvariable=hour)
minute_entry = Entry(root, width = 3,font = ('Arial',21,''), textvariable=minute)
second_entry = Entry(root, width = 3,font = ('Arial',21,''), textvariable=second)
#creating the btns
submit_btn = Button(root, text='Set Time Counter', bg='red', bd=4, fg='yellow', command=submit)



#all the placements
hour_entry.place(x=60,y=25)
minute_entry.place(x=135,y=25)
second_entry.place(x=205,y=25)
submit_btn.place(x=100,y=155)

root.mainloop()
