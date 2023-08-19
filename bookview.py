from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg


def book_list():

    root = Tk()
    Lb = Listbox(root, bg='#ff5733', font=('Courier New', 15))
    Lb.grid()
    f = open("book.txt", "r")
    for x in f:
        Lb.insert(END, x)
    f.close()
    root.mainloop()


def add():
    root = Tk()
    root.geometry("600x600")

    def bookappend():
        if nameentry.get() == "" or mobileentry.get() == "" or bentry.get() == "":
            tmsg.showerror("Eror", "Enter the values!")
            # top= Toplevel(root)
            # top.geometry("750x250")
            # top.title("Child Window")
            # Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)
        else:
            e = bentry.get()
            with open("book.txt", 'a') as f:
                f.write(f"\n { bentry.get()}")
                tmsg.showinfo(
                    "Submited..", "Thank you ! for donating this book!")
                root.destroy()

    f1 = Frame(root, bg="LightCoral", bd=5)
    f1.place(relx=0, rely=0, relwidth=1, relheight=1)

    f = Frame(f1, bg="black", bd=5)
    f.place(relx=0.3, rely=0.05, relwidth=0.5, relheight=0.13)
    Label(f, text="Information", bg="black", fg="#ff5733",
          font=('Courier', 20)).place(relx=0, rely=0, relwidth=1, relheight=1)
    name = Label(root, text="Enter your name", bg="LightCoral",
                 font=('Courier', 15)).place(relx=0.01, rely=0.3)
    mobile = Label(root, text="Enter your mobile", bg="LightCoral",
                   font=('Courier', 15)).place(relx=0.01, rely=0.5)
    book = Label(root, text="Enter Book Name", bg="LightCoral",
                 font=('Courier', 15)).place(relx=0.01, rely=0.6)

    gender = Label(f1, text="Gender", bg="LightCoral", font=(
        'Courier', 15)).place(relx=0.01, rely=0.4)

    gen1 = IntVar()
    Checkbutton(f1, text="Male", variable=gen1, bg="LightCoral",
                font=('Courier', 15)).place(relx=0.45, rely=0.4)
    gen2 = IntVar()
    Checkbutton(f1, text="Female", variable=gen2, bg="LightCoral",
                font=('Courier', 15)).place(relx=0.7, rely=0.4)

    nameentry = Entry(root, font="lucida,15,bold")
    mobileentry = Entry(root,  font="lucida,15,bold")
    bentry = Entry(root, font="lucida,15,bold")

    nameentry.place(relx=0.45, rely=0.3)
    mobileentry.place(relx=0.45, rely=0.5)
    bentry.place(relx=0.45, rely=0.6)

    b = Button(root, text="ADD Book", bg='black', fg="#ff5733",
               activebackground="#FBB195", font=('Courier New', 20), command=bookappend)
    b.place(relx=0.35, rely=0.75, relwidth=0.3, relheight=0.1)

    root.mainloop()


def issue():

    def bookremove():
        e = bentry.get()
        f = open("book.txt")
        t = f.read()
        if e in t:
            print("Twikle is present ")
            t = t.replace(e, " ")
            with open("book.txt", "w") as f:
                f.write(t)
                tmsg.showinfo(
                    "Issued..", "Congratulation ! you issed this book!")
                root.destroy()

        else:
            tmsg.showerror("Eror", "This book is not in this library.")
        return

    root = Tk()
    root.geometry("500x600")

    f1 = Frame(root, bg="LightCoral", bd=5)
    f1.place(relx=0, rely=0, relwidth=1, relheight=1)

    f = Frame(f1, bg="black", bd=5)
    f.place(relx=0.3, rely=0.05, relwidth=0.5, relheight=0.13)
    Label(f, text="Information", bg="black", fg="#ff5733",
          font=('Courier', 20)).place(relx=0, rely=0, relwidth=1, relheight=1)
    name = Label(root, text="Enter your name", bg="LightCoral",
                 font=('Courier', 15)).place(relx=0.01, rely=0.3)
    mobile = Label(root, text="Enter your mobile", bg="LightCoral",
                   font=('Courier', 15)).place(relx=0.01, rely=0.5)
    book = Label(root, text="Enter Book Name", bg="LightCoral",
                 font=('Courier', 15)).place(relx=0.01, rely=0.6)

    gender = Label(f1, text="Gender", bg="LightCoral", font=(
        'Courier', 15)).place(relx=0.01, rely=0.4)

    gen1 = IntVar()
    Checkbutton(f1, text="Male", variable=gen1, bg="LightCoral",
                font=('Courier', 15)).place(relx=0.45, rely=0.4)
    gen2 = IntVar()
    Checkbutton(f1, text="Female", variable=gen2, bg="LightCoral",
                font=('Courier', 15)).place(relx=0.7, rely=0.4)

    nameentry = Entry(root, font="lucida,15,bold")
    mobileentry = Entry(root,  font="lucida,15,bold")
    bentry = Entry(root, font="lucida,15,bold")

    nameentry.place(relx=0.45, rely=0.3)
    mobileentry.place(relx=0.45, rely=0.5)
    bentry.place(relx=0.45, rely=0.6)

    b = Button(root, text="Issue Book", bg='black', fg='#FF6700',
               activebackground="#FBB195", font=('Courier New', 20), command=bookremove)
    b.place(relx=0.35, rely=0.8, relwidth=0.4, relheight=0.1)

    root.mainloop()


def rbook():
    root = Tk()
    root.geometry("500x600")

    def bookreturn():
        if nameentry.get() == "" or mobileentry.get() == "" or bentry.get() == "":
            tmsg.showerror("Eror", "Enter the values!")
        else:
            e = bentry.get()
            with open("book.txt", 'a') as f:
                f.write(f"\n { bentry.get()}")
                tmsg.showinfo(
                    "Returned..", "Thank you ! for retuning this book!")
                root.destroy()

        # print(bvalue.get())
        print("appende")

    f1 = Frame(root, bg="LightCoral", bd=5)
    f1.place(relx=0, rely=0, relwidth=1, relheight=1)

    f = Frame(f1, bg="black", bd=5)
    f.place(relx=0.3, rely=0.05, relwidth=0.5, relheight=0.13)
    Label(f, text="Information", bg="black", fg="#ff5733",
          font=('Courier', 20)).place(relx=0, rely=0, relwidth=1, relheight=1)
    name = Label(root, text="Enter your name", bg="LightCoral",
                 font=('Courier', 15)).place(relx=0.01, rely=0.3)
    mobile = Label(root, text="Enter your mobile", bg="LightCoral",
                   font=('Courier', 15)).place(relx=0.01, rely=0.5)
    book = Label(root, text="Enter Book Name", bg="LightCoral",
                 font=('Courier', 15)).place(relx=0.01, rely=0.6)

    gender = Label(f1, text="Gender", bg="LightCoral", font=(
        'Courier', 15)).place(relx=0.01, rely=0.4)

    gen1 = IntVar()
    Checkbutton(f1, text="Male", variable=gen1, bg="LightCoral",
                font=('Courier', 15)).place(relx=0.45, rely=0.4)
    gen2 = IntVar()
    Checkbutton(f1, text="Female", variable=gen2, bg="LightCoral",
                font=('Courier', 15)).place(relx=0.7, rely=0.4)

    nameentry = Entry(root, font="lucida,15,bold")
    mobileentry = Entry(root,  font="lucida,15,bold")
    bentry = Entry(root, font="lucida,15,bold")

    nameentry.place(relx=0.45, rely=0.3)
    mobileentry.place(relx=0.45, rely=0.5)
    bentry.place(relx=0.45, rely=0.6)

    b = Button(root, text="Return Book", bg='black', fg='#FF6700',
               activebackground="#FBB195", font=('Courier New', 20), command=bookreturn)
    b.place(relx=0.35, rely=0.8, relwidth=0.4, relheight=0.1)

    root.mainloop()
