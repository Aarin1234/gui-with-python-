from tkinter import*
root = Tk()
root.title('Create Replit template!')
root.geometry('400x250')
#pick a template label and text box creation
template_label = Label(root, text='Pick a template(1, 2 or 3)')
template_label.place(x=135, y=35)

template_label_input_area = Entry(root, width=30)
template_label_input_area.place(x=110, y=58)
#name your project
project_name = Label(root, text='Name your project')
project_name.place(x=158, y=95)

project_name_input_area = Entry(root, width=30)
project_name_input_area.place(x=110, y=118)
#create repl button
btn = Button(root, text = 'Create repl', background="#4CAF50",
              activebackground="#1967C0", activeforeground='white')
btn.place(x=165, y=148)
root.mainloop()