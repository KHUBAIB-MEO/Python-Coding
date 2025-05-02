import tkinter as tk 

root = tk.Tk()
root.geometry("600x600")

num1Label = tk.Label(root, text = "Number 1")
num1Label.grid(row = 0, column = 3)

num1Entry = tk.Entry(root, width = 30)
num1Entry.grid(row = 0, column = 8, padx = 30)

num2Label = tk.Label(root, text = "Number 2")
num2Label.grid(row = 0, column = 15)

num2Entry = tk.Entry(root, width = 30)
num2Entry.grid(row = 0, column = 16, padx = 30)

root.mainloop()