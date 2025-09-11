from tkinter import *
hello= Tk()
hello.geometry('600x600')#where to create the button
btn = Button(hello, text = 'Click me!', bd= 6, background='blue',
              activebackground='green', activeforeground='red',)
btn.pack(side = 'top')


btn = Button(hello, text = 'Hello', bd= 6, background='red',
              activebackground='black', activeforeground='yellow',)
btn.pack(side = 'bottom')


btn = Button(hello, text = 'e!', bd= 6, background='green',
              activebackground='blue', activeforeground='orange',)
btn.pack(side = 'right')


btn = Button(hello, text = 'test', bd= 6, background='yellow',
              activebackground='white', activeforeground='blue',)
btn.pack(side = 'left')


hello.mainloop()