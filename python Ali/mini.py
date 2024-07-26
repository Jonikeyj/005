
from tkinter import *

def red_black():
    root.configure(bg="#e8e8e8")
    frame["bg"] = "#e8e8e8"
root = Tk()
root.title("mmmmmyyyyy ")
root.geometry("500x500")
root.configure(bg="#e8e8e8")

title = Label(root, text="my mego proekt", bg="#a30202", fg="#000000")
title.pack()

frame = Frame(root, bg="#000000")
frame.pack(anchor="center")

btn1 = Button(frame, text="btn1", fg="#e8e8e8", bg="#000000", command=red_black)
btn2 = Button(frame, text="red", font=("Comic Sans MS", 12, 'bold'))
btn3 = Button(frame, text="btn3")
btn4 = Button(frame, text="btn4")

btn1.grid(row=0, column=3, pady=10, padx=10)
btn2.grid(row=1, column=2, pady=10, padx=10)
btn3.grid(row=2, column=1, pady=10, padx=10)
btn4.grid(row=3, column=0, pady=10, padx=10)

root.mainloop()