import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox

root = tk.Tk()
root.geometry("500x500")

#----------------------------clicked function----------------------------#
def clicked():
    messagebox.showinfo("Alert", f"Welcome {name.get()}")

#----------------------------Entry Widget----------------------------#
name = tk.Entry(root, width = 20)
name.pack(pady = 10)

#----------------------------Button Widget----------------------------#
button1 = tk.Button(root, text = "Enter", command = clicked)
button1.pack()

#----------------------------Combo Box Widget----------------------------#
combo = Combobox(root)
combo["values"] = (1, 2, 3, 4, 5, "Text")
combo.current(0)
combo.pack(pady = 10)

#----------------------------Chech Box Widget----------------------------#
checkBox = BooleanVar()
checkBox.set(False)
cBox = Checkbutton(root, text = "Select", var = checkBox)
cBox.pack()

#----------------------------Radio Button Widget----------------------------#
selected = tk.IntVar()
selected.set(1)
rad1 = Radiobutton(root, text = "AI", value = 1, variable = selected)
rad1.pack()
rad2 = Radiobutton(root, text = "CCN", value = 2, variable = selected)
rad2.pack()
rad3 = Radiobutton(root, text = "SPM", value = 3, variable = selected)
rad3.pack()

#----------------------------Spin Box Widget----------------------------#
spin = Spinbox(root, from_= 1, to = 100, width = 10)
spin.pack()

#----------------------------Button2 position check----------------------------#
button2 = tk.Button(root, text = "Button 2").pack(side = "left")

#----------------------------Login----------------------------#
def Clicked():
    print("username entered :", username.get())
    print("password entered :", password.get())

tk.Label(root, text = "Username").pack()
username = StringVar()
tk.Entry(root,textvariable=username).pack()
tk.Label(root, text = "Password").pack()
password = StringVar()
tk.Entry(root,textvariable=password,show='*').pack()
tk.Button(root, text="Login", command=Clicked).pack()


root.mainloop()


