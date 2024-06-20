import random
import tkinter
from tkinter import font,Button, Entry, Label, Tk, messagebox
from tkinter.ttk import Combobox
from tkinter.font import Font

ww = Tk()
ww.title("PASSWORD GENERATOR")
ww.geometry("600x300+300+200")
# Configure font
fstyle= font.Font(family="Arial", size=15)
f1 = ("arial", 15, 'bold')
f2 = ("calibre", 14)
global password
def generate():
    global password
    password = ''
    try:
        length = int(e1.get())
        difficulty = c1.current()
        if length < 6 or length > 20:
            print(difficulty)
            messagebox.showinfo("Invalid Length", "Please provide length in between 6 to 20")
            return
        else:
            if difficulty == -1:
                messagebox.showinfo("Invalid difficulty", "Please provide difficulty of password")
                return
            if difficulty == 0:  # Easy
                while length > 0:
                    password += str(random.randint(0, 9))
                    length -= 1
                l4.config(text=password)
            elif difficulty == 1:  # Medium
                alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                while length > 0:
                    switch2 = random.randint(1, 2)
                    if switch2 == 1:
                        password += str(random.randint(0, 9))
                    elif switch2 == 2:
                        password += random.choice(alpha)
                    length -= 1
                l4.config(text=password)
            elif difficulty == 2: # Difficult
                alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                symbols = "!@#$%^&*()-+;:'|,<.>/?`~"
                while length > 0:
                    switch3 = random.randint(1, 3)
                    if switch3 == 1:
                        password += str(random.randint(0, 9))
                    elif switch3 == 2:
                        password += random.choice(alpha)
                    elif switch3 == 3:
                        password += random.choice(symbols)
                    length -= 1
                l4.config(text=password)
    except ValueError:
        messagebox.showinfo("Invalid Length", "Please provide valid value")
l1 = Label(ww, text="ENTER PASSWORD LENGTH :", font=f1)
l1.place(x=15, y=40)
e1 = Entry(ww, font=f2)
e1.place(x=350, y=40)

l2 = Label(ww, text="SET PASSWORD COMPLEXITY :", font=f1)
l2.place(x=15, y=100)
data = ["EASY (INT)", "MEDIUM (INT + ALPHABETS)", "HARD (INT + ALPHABETS + SYMBOLS)"]
c1 = Combobox(values=data)
c1.config(width=30)
c1.place(x=350, y=100)

b1 = Button(ww, text="GENERATE", font=f1, command=generate)
b1.place(x=250, y=160)

l3 = Label(ww, text="PASSWORD :", font=f1)
l3.place(x=180, y=230)

l4 = Label(ww, text="- - - - -", font=f2)
l4.place(x=320, y=230)

CL = tkinter.Label(ww, text="PASSWORD GENERATOR", wraplength=400,font=Font(family="Arial", size=15, weight="bold"), fg="red")
CL.pack()
ww.mainloop()
