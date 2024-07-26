from tkinter import *
import os
import webbrowser

def open_pit():
    os.system("mspaint")

def open_yt():
    webbrowser.open("https://m.youtube.com/?hl=ru")

root = Tk()
root.title("управление системой")
root.geometry("500x150")

btn1 = Button(text="открыть Paint", command=open_pit)
btn2 = Button(text="открыть YouTube", command=open_yt)

btn1.pack(pady=10)
btn2.pack(pady=10)























root.mainloop()