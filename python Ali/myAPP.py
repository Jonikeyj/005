from tkinter import *

def get_entry():
    value = int(entry.get())
    value1 = int(entry2.get())
    value2 = int(entry3.get())
    value3 = int(entry4.get())
    txt["text"] = value + value1 * value2 / value3

root = Tk()
root.title("mmmmmyyyyy ")
root.geometry("500x500")

entry = Entry()
entry.pack()

entry2 = Entry()
entry2.pack()

entry3 = Entry()
entry3.pack()

entry4 = Entry()
entry4.pack()

txt = Label(text="nnew tex...")
txt.pack()

btn = Button(text="click", command=get_entry)
btn.pack()














































root.mainloop()