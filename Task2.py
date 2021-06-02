from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Donation Page")
window.geometry("600x600")
window.config(bg="aqua")


def clear_btn():
    e1.delete(0, END)


def exit_btn():
    return window.destroy()


def right_amount():
    try:
        amount = 3000
        if int(e1.get()) >= amount:
            messagebox.showinfo(title="STATUS", message="Congratulations. You qualify to go to Malaysia.")
    except ValueError:
        if e1.get() != int:
            messagebox.showerror(title="Error", message="Invalid! Amount must be an integer")
    else:
        if int(e1.get()) < amount:
            messagebox.showerror(title="Error", message="Sorry you do not qualify to go to Malaysia.")


lab1 = Label(window, text="Please enter amount in your account: ")
lab1.place(x=10, y=10)

e1 = Entry(window)
e1.place(x=270, y=10)

b1 = Button(window, text="Check Qualification", command=right_amount)
b1.config(bg="#ed2d34")
b1.place(x=10, y=70)
b2 = Button(window, text="Clear", command=clear_btn)
b2.place(x=170, y=70)
b3 = Button(window, text="Exit", command=exit_btn)
b3.place(x=235, y=70)

window.mainloop()
