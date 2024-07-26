from tkinter import *

# def get_entry():
#     v1 = int(entry1.get())
#     v2 = int(entry2.get())
#     v3 = int(entry3.get())
#     txt["text"] = v1 + v2 - v3

def get_entry():
    v1 = entry1.get()
    v2 = entry2.get()
    v3 = entry3.get()
    
    if v1 == '' or v2 == '' or v3 == '':
        txt["text"] = 'заполните все поля'
        txt["bg"] = '#f51111'
        return
    else:
        if v2 != '+' and v2 != '-' and v2 != '/' and v2 != "*":
            txt["text"] = "неверная операция"
            txt["bg"] = '#f51111'
        else:
            if v2 == '+':
                txt["text"] = float(v1) + float(v3)
                txt["bg"] = '#33f511'
            else:
                if v2 == '-':
                    txt["text"] = float(v1) - float(v3)
                    txt["bg"] = '#33f511'
                else:
                    if v2 == '/':
                        txt["text"] = float(v1) / float(v3)
                        txt["bg"] = '#33f511'
                    else:
                        if v2 == '*':
                            txt["text"] = float(v1) * float(v3)
                            txt["bg"] = '#33f511'

root = Tk()
root.title = "my app"
root.geometry("670x400")

frame = Frame(root)
frame.pack(anchor="center")

lab1 = Label(frame, text="число", font=("Comic Sans MS", 12, 'bold'))
lab2 = Label(frame, text="операция", font=("Comic Sans MS", 12, 'bold'))
lab3 = Label(frame, text="число", font=("Comic Sans MS", 12, 'bold'))
entry1 = Entry(frame, font=("Comic Sans MS", 12, 'bold'))
entry2 = Entry(frame, font=("Comic Sans MS", 12, 'bold'))
entry3 = Entry(frame, font=("Comic Sans MS", 12, 'bold'))
btn = Button(frame, text="вычисление",font=("Comic Sans MS", 12, 'bold'), command=get_entry)
txt = Label(frame, text="")

lab1.grid(row=0, column=0, padx=10, pady=10)
lab2.grid(row=0, column=1, padx=10, pady=10)
lab3.grid(row=0, column=2, padx=10, pady=10)
entry1.grid(row=1, column=0, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)
entry3.grid(row=1, column=2, padx=10, pady=10)
btn.grid(row=2, column=0, columnspan=3, sticky="we", padx=10, pady=10)
txt.grid(row=3, column=0, columnspan=3, sticky="we", padx=10, pady=10)











root.mainloop()