from tkinter import *
import time

window = Tk()
def lol():
    print("hello")
    but.config(text = "fwqfwe")
    but.config(command = go)
def go():
    print("lll")
but = Button(window, text = "lol", command = lol)
but.pack()


window.mainloop()