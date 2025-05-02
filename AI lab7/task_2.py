import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x600")
root.title("Registration form")

def clicked():
    messagebox.showinfo("User",f"Name = {nameEntry.get()}\nContact = {contactEntry.get()}\nEmail = {emailEntry.get()}\nREGISTRATION COMPLETE SUCCESSFULLY")

nameLabel = tk.Label(root, text = "Name*")
nameLabel.grid(padx = 50, pady = 30)

nameEntry = tk.Entry(root, width = 30)
nameEntry.grid(row = 0, column = 10)

contactLabel = tk.Label(root, text = "Contact*")
contactLabel.grid(padx = 50, pady = 30)

contactEntry = tk.Entry(root, width = 30)
contactEntry.grid(row = 1, column = 10)

emailLabel = tk.Label(root, text = "Email*")
emailLabel.grid(padx = 50, pady = 30)

emailEntry = tk.Entry(root, width = 30)
emailEntry.grid(row = 2, column = 10)

genderLabel = tk.Label(root, text = "Gender*")
genderLabel.grid( pady = 30)

genderSecleted = tk.IntVar()
maleRadioButton = tk.Radiobutton(root, text = "MALE", value = 1, variable = genderSecleted)
maleRadioButton.grid(row = 3, column = 10)
femaleRadioButton = tk.Radiobutton(root, text = "FEMALE", value = 2, variable = genderSecleted)
femaleRadioButton.grid(row = 3, column = 20)

cityLabel = tk.Label(root, text = "City*")
cityLabel.grid( pady = 30)

citySelect = Combobox()
citySelect['values'] = ("Karachi", "Lahore", "Islamabad", "Multan", "Sialkot", "Hyderabad", "Rawalpindi", "Peshawar", "Quetta", "Faisalabad")
citySelect.current(0)
citySelect.grid(column = 10, row = 4)

provinceLabel = tk.Label(root, text = "City*")
provinceLabel.grid( pady = 30)

provinceSelect = Combobox()
provinceSelect['values'] = ("Sindh", "Punjab", "Balochistan", "KPK")
provinceSelect.current(0)
provinceSelect.grid(column = 10, row = 5)

registerButton = tk.Button(root, text = "Register", command = clicked)
registerButton.grid(row = 6, column = 10)
root.mainloop()