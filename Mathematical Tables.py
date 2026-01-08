from tkinter import*
from tkinter.ttk import*
#import tkinter.font as font
#creating the window
window = Tk()
window.geometry('375x750')
window.title('Mathematical Tables Generater')
window.configure(bg='green')


def generate_math_table():
    tables =""
    for i in range(1,endval.get()+1):
        tables+=str(theNum.get()) +" X "+str(i) +" = "+str(theNum.get()*i)+"\n"
    table.configure(text=tables)


table=Label(window,anchor="center")

game_title = Label(window,text='Mathematical Table',background='white',foreground='black',font=('Arial', 16, 'bold'))

caption = Label(window, text='Number & Range', background='white',foreground='red', font=('Arial', 13))


#combobox
theNum = IntVar()
numbers = Combobox(window, textvariable= theNum, width=5)
numbers['values'] = tuple(range(101))


#radio btns
endval = IntVar()
r10 = Radiobutton(window, text='10', variable=endval, value=10)
r20 = Radiobutton(window, text='20',variable=endval, value=20)
r30 = Radiobutton(window, text='30',variable=endval, value=30)
endval.set(10)


#creating the btns
generate_btn = Button(window, text='generate table', command=generate_math_table)


#all placements
game_title.place(x=92,y=40)
caption.place(x=35,y=135)
numbers.place(x=205,y=135)
r10.place(x=295,y=135)
r20.place(x=295,y=155)
r30.place(x=295,y=175)
generate_btn.place(x=200,y=195)
table.place(x=205,y=250)



window.mainloop()
