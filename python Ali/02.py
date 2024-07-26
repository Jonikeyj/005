from tkinter import *

user_info = {"name": "admin", "password": "12345"}


def frame_1():
    user_name = user_name_entry.get()
    user_pass = user_pass_entry.get()




    if user_name == user_info["name"] and user_pass == user_info["password"]:
        frame1.pack_forget()
        frame2.pack(fill='both', expand=True)
    else:
        frame2.pack_forget()
        frame1.pack(fill='both', expand=True)

root = Tk()
root.title("многоокное предложение ")
root.geometry("300x200")

frame1 = Frame(root)
frame2 = Frame(root)

label1 = Label(frame1, text="первое окно")
label1.pack(padx=10, pady=10)

label2 = Label(frame2, text="второе окно")
label2.pack(padx=10, pady=10)
button = Button(root, text="pereklychit okno", command=frame_1)
button.pack()

user_name_entry = Entry(frame1)
user_pass_entry = Entry(frame1)
user_name_entry.pack()
user_pass_entry.pack()

frame1.pack(fill='both', expand=True)




























root.mainloop()



















