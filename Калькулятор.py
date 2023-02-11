from tkinter import *
from tkinter import messagebox


def button_1():
    messagebox.showinfo('Результат', float(a.get()) * float(b.get()))


def button_2():
    messagebox.showinfo('Результат', float(a.get()) - float(b.get()))


def button_3():
    messagebox.showinfo('Результат', float(a.get()) + float(b.get()))


def button_4():
    messagebox.showinfo('Результат', float(a.get()) / float(b.get()))


def button_5():
    messagebox.showinfo('Результат', float(a.get()) // float(b.get()))


def button_6():
    messagebox.showinfo('Результат', float(a.get()) % float(b.get()))


root = Tk()
root.title('Калькулятор')
root.geometry('300x300')
a = Entry(root, width=10, bg='gray', fg='white', font='consolas')
a.pack()
b = Entry(root, width=10, bg='gray', fg='white', font='consolas')
b.pack()
Button(root, text='*', width=10, height=1, command=button_1, \
       bg='white').pack()
Button(root, text='-', width=10, height=1, command=button_2, \
       bg='white').pack()
Button(root, text='+', width=10, height=1, command=button_3, \
       bg='white').pack()
Button(root, text='/', width=10, height=1, command=button_4, \
       bg='white').pack()
Button(root, text='//', width=10, height=1, command=button_5, \
       bg='white').pack()
Button(root, text='%', width=10, height=1, command=button_6, \
       bg='white').pack()
root.mainloop()