from tkinter import *

window = Tk()
window.title("Keyboard Practice")
window.geometry("400x300")

def handle_keypress(event):
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nThe button was clicked")

def handle_click2(event):
    print("\nHELLO Button was clicked")

def handle_click3(event):
    print("\nGOODBYE Button was clicked")

button = Button(window, text="Click Me")
button2 = Button(window, text="HELLO Button")
button3 = Button(window, text="GOODBYE Button")
button.pack()
button2.pack()
button3.pack()
button.bind("<Button-1>", handle_click)
button2.bind("<Button-1>", handle_click2)
button3.bind("<Button-1>", handle_click3)

window.mainloop()