# myList = [0, 53, 78, 32, 20, 7, 55, 67, 4, 3, 9, 10, 86]


# print(myList.sort())
# print(myList)

# myList2 = [0, 53, 78, 32, 20, 7, 55, 67, 4, 3, 9, 10, 86]


# print(sorted(myList2))
# print(myList2)

# import sup
# import time

# sup.hello()

# time.sleep(5)

# sup.sum(10, 20)

# from sup import hello
# hello()
# class Person:
#   num1 = 10

# x1 = person()
# print(x1.num1)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def hello(self):
#     print(f"привет меня зовут {self.name}")

# one_person = Person("Stenli", 20)
# print(one_person.name)
# print(one_person.age)
# one_person.hello()



# from tkinter import *

# clicks = 0
# clicks1 = 0
# def finish():
#   root.destroy()
#   print("App is close")

# def click_button():
#   global clicks
#   clicks += 999
#   btn5["text"] = f"clicks {clicks}"

# def click_buttonn():
#   global clicks1
#   clicks1 -= 999
#   btn5["text"] = f"clicks1 {clicks1}"

# root = Tk()
# root.title("my vvvvv")
# root.geometry("500x300")
# root.minsize(200, 200)
# root.maxsize(1200, 1200)
# # root.resizable(False, False)
# # root.attributes("-fullscreen", True)
# # root.attributes("-alpha", 100)
# root.protocol("WM_DELETE_WINDOW", finish)

# icon = PhotoImage(file="str.png")
# root.iconphoto(True, icon)

# label = Label(text="Hello my friend")
# label.pack()

# btn1 = Button(text="Click")
# btn1.pack()
# btn2 = Button()
# btn2.pack()
# btn2["text"] = "no click"

# btn3 = Button()
# btn3.pack()

# btn5 = Button(text="Click", command=click_button)
# btn5.pack()

# btn6 = Button(text="Click1", command=click_buttonn)
# btn6.pack()







# root.mainloop()



from tkinter import *

def get_entry():
    value = entry.get()
    txt["text"] = value

root = Tk()
root.title("mmmmmyyyyy ")
root.geometry("500x500")

icon = PhotoImage(file="str.png")


entry = Entry()
entry.pack()

txt = Label(text="nnew tex...")
txt.pack()

btn = Button(text="click", command=get_entry)
btn.pack()


root.mainloop()