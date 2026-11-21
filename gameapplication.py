from tkinter import *
from datetime import date

root = Tk()
root.title("Game Application")
root.geometry("800x600")

lbl = Label(text="Welcome to the Game Application!", fg = "white", bg = "black", height = 1, width = 300)
name_lbl = Label(text = "Enter your name: ", fg = "white", bg = "black")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to the application, today's date is"
    greet = "Hello" + name + "\n"
    text_box.insert(END, greet)
    text_box.insert(END, date.today)
text_box = Text(height=10)
btn = Button(text = "Begin", command = display, height = 1, bg = "black", fg = "white")

lbl.pack()
name_lbl.pack()
name_entry.pack()
text_box.pack()
btn.pack()

root.mainloop()
