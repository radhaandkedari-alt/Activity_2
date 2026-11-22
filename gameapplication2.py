from tkinter import *

root = Tk()
root.title("Number Pad")
root.geometry("400x300")

frame = Frame(master = root)
nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ['#', 0, '*']
    ['/', 11, '-']
]

for i in range(5):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
    for j in range(0, 3):
        frame = Frame(
            master=root,
            relief=FLAT,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = Label(master=frame, text=nums[i][j], bg = "Brown", fg = "White")
        label.pack(padx=10, pady=10)
root.mainloop()