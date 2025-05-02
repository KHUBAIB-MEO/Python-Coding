import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.geometry("600x600")

def clicked():
    if username.get() == "Khubaib" and password.get() == "15045":
        messagebox.showinfo("Login", f"Login successfully")
    else:         
        messagebox.showinfo("Login", f"Login unsuccessfully")

tk.Label(root, text = "Username").pack()
username = tk.StringVar()
tk.Entry(root,textvariable=username).pack()
tk.Label(root, text = "Password").pack(pady = 10)
password = tk.StringVar()
tk.Entry(root,textvariable=password,show='*').pack()
tk.Button(root, text="Login", command=clicked).pack()

root.mainloop()