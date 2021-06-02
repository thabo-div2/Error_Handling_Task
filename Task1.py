from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login")
root.geometry("650x650")
root.config(bg="#555555")


def exit_btn():
    return root.destroy()


def clear_btn():
    name_entry.delete(0, END)
    password_entry.delete(0, END)


def membership():
    usernames = {"Thabo": "Lion", "Oscar": "Cheetah", "Ayanda": "Leopard", "Mujaid": "Panther"}

    if usernames.get(name_entry.get()):
        if usernames[name_entry.get()] == password_entry.get():
            messagebox.showinfo("Message", "Access Granted")
            root.destroy()
            import Task2
        else:
            messagebox.showerror(title="Error", message="Access Denied!!!")


myframe = Frame(root, bg="#ed2d34")
myframe.place(x=10, y=10, width=600, height=550)

name = Label(myframe, text="Username: ")
name.place(x=10, y=20)
password = Label(myframe, text="Password: ")
password.place(x=10, y=70)

name_entry = Entry(myframe)
name_entry.place(x=100, y=20)
password_entry = Entry(myframe, show="*")
password_entry.place(x=100, y=70)

b1 = Button(myframe, text="Login", command=membership)
b1.place(x=10, y=150)
b2 = Button(myframe, text="Clear", command=clear_btn)
b2.place(x=80, y=150)
b3 = Button(myframe, text="Exit", command=exit_btn)
b3.place(x=150, y=150)

root.mainloop()
