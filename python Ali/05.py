from tkinter import *

def get_entry():
    v1 = entry1.get()
    if v1 == '':
        txt["text"] = 'заполните полe'
        txt["bg"] = '#f51111'
        return
    else:
        if v1:
            txt["text"] = f"{round(float(v1) / 86)}$"
            txt["bg"] = '#33f511'       
        if v1:
            txt1["text"] = f"{round(float(v1) / 96)}evro"
            txt1["bg"] = '#33f511'
        if v1:
            txt2["text"] = f"{round(float(v1) * 3)}Tenge"
            txt2["bg"] = '#33f511'
        if v1:
            txt3["text"] = f"{round(float(v1) / 0.9)}p"
            txt3["bg"] = '#33f511'






root = Tk()
root.title = "my app"
root.geometry("235x330")
root.minsize(235, 330)
root.maxsize(235, 330)

frame = Frame(root)
frame.pack(anchor="center")

label1 = Label(frame, text="ввывод", font=("Comic Sans MS", 12, 'bold'))
entry1 = Entry(frame, font=("Comic Sans MS", 12, 'bold'))
btn = Button(frame, text="вычисление",font=("Comic Sans MS", 12, 'bold'), command=get_entry)
txt = Label(frame, text="")
txt1 = Label(frame, text="")
txt2 = Label(frame, text="")
txt3 = Label(frame, text="")

label1.grid(row=0, column=0, padx=10, pady=10)
entry1.grid(row=1, column=0, padx=10, pady=10)
btn.grid(row=2, column=0, columnspan=3, sticky="we", padx=10, pady=10)
txt.grid(row=3, column=0, columnspan=3, sticky="we", padx=10, pady=10)
txt1.grid(row=4, column=0, columnspan=3, sticky="we", padx=10, pady=10)
txt2.grid(row=5, column=0, columnspan=3, sticky="we", padx=10, pady=10)
txt3.grid(row=6, column=0, columnspan=3, sticky="we", padx=10, pady=10)



















root.mainloop()