import tkinter as tk
import math

def quadratic_equation():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    
    discriminant = b**2 - 4*a*c

    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        result_label.configure(text=f"RESULT D: {discriminant:.2f}, x1: {root1:.2f}, x2: {root2:.2f}", bg='lightgreen', fg='blue')
    else:
        result_label.configure(text=f"Lahendus D: {discriminant:.2f}, No real roots", bg='blue')
    

root = tk.Tk()
root.title("Quadratic Equation Solver")
root.geometry('300x300')

a_label = tk.Label(root, text="a:",fg='#d30085',font='Arial 15',height=1,width=15)
a_label.pack()
a_entry = tk.Entry(root, bg='#99ffe5')
a_entry.pack()

b_label = tk.Label(root, text="sisesta b:", fg='#d30085',font='Arial 15',height=1,width=15)
b_label.pack()
b_entry = tk.Entry(root, bg='#99ffe5')
b_entry.pack()

c_label = tk.Label(root, text="sisesta c:", fg='#d30085',font='Arial 15',height=1,width=15)
c_label.pack()
c_entry = tk.Entry(root, bg='#99ffe5')
c_entry.pack()

solve_button = tk.Button(root, text="Salvesta", command=quadratic_equation)
solve_button.pack()


result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()


    
