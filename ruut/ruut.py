from tkinter import *
from math import *
import numpy as np
import matplotlib.pyplot as plt


def quad():
    if a_entry.get()=='' :
        a_entry.configure(bg='red')
    else:
        a_entry.configure(bg='lightblue')
    if b_entry.get()=='' :
        b_entry.configure(bg='red')
    else:
        b_entry.configure(bg='lightblue')
    if c_entry.get()=='' :
        c_entry.configure(bg='red')
    else:
        c_entry.configure(bg='lightblue')
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    D = b**2 - 4*a*c

    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        result_lbl.configure(text=f'TULEMUS - D: {D:.2f}, x1: {x1:.2f}, x2: {x2:.2f}', bg='lightgreen', fg='blue')
    else:
        result_lbl.configure(text=f'Lahendus D: {D:.2f}, pole tõelisi juured', bg='lightgreen')
    x0=(-b)/2*a
    y0=a*x0**2+b*x0+c
    x=np.arange(x0-15,x0+15,1)
    y=a*x**2+b*x+c
    fig=plt.figure()
    plt.plot(x,y,'r-d')
    plt.title('Ruudvõrrand')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.grid(True)
    plt.show()

    

root = Tk()
root.title('Rootvõrrandid')
root.geometry('300x300')

a_lbl = Label(root, text='sisesta a:',fg='#d30085',font='Arial 15',height=1,width=15)
a_lbl.pack()
a_entry = Entry(root, bg='#99ffe5')
a_entry.pack()

b_lbl = Label(root, text='sisesta b:', fg='#d30085',font='Arial 15',height=1,width=15)
b_lbl.pack()
b_entry = Entry(root, bg='#99ffe5')
b_entry.pack()

c_lbl = Label(root, text='sisesta c:', fg='#d30085',font='Arial 15',height=1,width=15)
c_lbl.pack()
c_entry = Entry(root, bg='#99ffe5')
c_entry.pack()

solve_button = Button(root, text='Lahenda', command=quad)
solve_button.pack()


result_lbl = Label(root, text='')
result_lbl.pack()


root.mainloop()


    
