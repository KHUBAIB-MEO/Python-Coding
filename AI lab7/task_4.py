import tkinter as tk 

root = tk.Tk()
root.geometry("600x600")
root.title("Calculator")

def add():
    result = int(num1Entry.get()) + int(num2Entry.get())
    resultLabel.configure(text = f"{result}")
def sub():
    result = int(num1Entry.get()) - int(num2Entry.get())
    resultLabel.configure(text = f"{result}")

def multiply():
    result = int(num1Entry.get()) * int(num2Entry.get())
    resultLabel.configure(text = f"{result}")

def divide():
    result = float(num1Entry.get()) / float(num2Entry.get())
    resultLabel.configure(text = f"{result}")

num1Label = tk.Label(root, text = "Number 1")
num1Label.grid(row = 0, column = 1)

num1Entry = tk.Entry(root, width = 30)
num1Entry.grid(row = 0, column = 2)

num2Label = tk.Label(root, text = "Number 2")
num2Label.grid(row = 0, column = 3)

num2Entry = tk.Entry(root, width = 30)
num2Entry.grid(row = 0, column = 4)

addBtn = tk.Button(root, text = "+", command = add,width = 10)
addBtn.grid(row = 1, column = 1,pady = 10)

subBtn = tk.Button(root, text = "-", command = sub,width = 10)
subBtn.grid(row = 1, column = 2,pady = 10)

multiplyBtn = tk.Button(root, text = "x", command = multiply,width = 10)
multiplyBtn.grid(row = 1, column = 3,pady = 10)

divideBtn = tk.Button(root, text = "/", command = divide,width = 10)
divideBtn.grid(row = 1, column = 4,pady = 10)

resultLabel = tk.Label(root, text = "0")
resultLabel.grid(row = 3, column = 3,pady = 20 )
root.mainloop()