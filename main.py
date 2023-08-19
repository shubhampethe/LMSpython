from tkinter import *
from PIL import Image, ImageTk
from bookview import *
def login():
    # top = Tk()
    # top.geometry("1500x800")
    # top.minsize(width=1500, height=800)
    # top.maxsize(width=1500, height=800)
    # f = Frame(top, bg="LightCoral", bd=5)
    # f.place(relx=0, rely=0, relwidth=1, relheight=1)
    # image = Image.open("lib.jpg")
    # image = image.resize((1500, 800), Image.ANTIALIAS)
    # photo = ImageTk.PhotoImage(image)
    # photo_label = Label(top, image=photo)
    # photo_label.grid()

    # image = Image.open("lib.jpg")
    # image = image.resize((1500, 800), Image.ANTIALIAS)
    # photo = ImageTk.PhotoImage(image)
    # bg=PhotoImage(file="lg.png")
    # l=Label(top,image=bg)
    # l.place(x=0,y=0)

        # if nameentry.get() == "" or mobileentry.get() == "" or bentry.get() == "":
        #     tmsg.showerror("Eror", "Enter the values!")
        #     # top= Toplevel(root)
        #     # top.geometry("750x250")
        #     # top.title("Child Window")
        #     # Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)
        # else:
        #     e = bentry.get()
        #     with open("book.txt", 'a') as f:
        #         f.write(f"\n { bentry.get()}")
        #         tmsg.showinfo(
        #             "Submited..", "Thank you ! for donating this book!")
        #         root.destroy()

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
               activebackground="#FBB195", font=('Courier New', 20))
    b.place(relx=0.35, rely=0.75, relwidth=0.3, relheight=0.1)

    root.mainloop()

    def about():
        tmsg.showinfo(
            "About us", "welcome ! This is programers library.Created by Shubham")
        # global pop
        # pop=Toplevel(top)
        # pop.title("About us")
        # pop.config(bg="pink")
        # pop_label=Label(pop,
        #       text="Welcome to Programmers library ! Created by Shubham",font=("Engravers MT",10))
        # pop_label.pack(pady=10)


    f1 = Frame(top, bg="#FFBB00", bd=5)
    f1.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.16)
    # Label(top, text="Welcome !", font=('Harlow Solid Italic', 40),
    #       bg="#641e16", fg="white").place(relx=0.001, rely=0)
    Label(f1, text="Programmer`s library", fg="#FFBB00", bg="black",
        font=('Algerian', 40), padx=50, pady=20).place(relx=0, rely=0, relwidth=1, relheight=1)

    b1 = Button(top, text="Add Book Details", bg='black', fg='#FF6700',
                activebackground="#FBB195", font=('Courier New', 20), command=add)
    b1.place(relx=0.1, rely=0.35, relwidth=0.3, relheight=0.1)

    b2 = Button(top, text="View Book List", bg='black', fg='#FF6700',
                activebackground="#FBB195", font=('Courier New', 20), command=book_list)
    b2.place(relx=0.1, rely=0.45, relwidth=0.3, relheight=0.1)

    b3 = Button(top, text="Issue Book to Student", bg='black',
                fg='#FF6700', activebackground="#FBB195", font=('Courier New', 20), command=issue)
    b3.place(relx=0.1, rely=0.55, relwidth=0.3, relheight=0.1)

    b4 = Button(top, text="Return Book", bg='black', fg='#FF6700',
                activebackground="#FBB195", font=('Courier New', 20), command=rbook)
    b4.place(relx=0.1, rely=0.65, relwidth=0.3, relheight=0.1)

    b5 = Button(top, text="About us", bg='black', fg='#FF6700',
                activebackground="#FBB195", font=('Courier New', 20), command=about)
    b5.place(relx=0.1, rely=0.75, relwidth=0.3, relheight=0.1)

    b6 = Button(top, text="Exit", bg='red', fg='black',
                activebackground="#FBB195", font=('Courier New', 15), command=top.destroy)
    b6.place(relx=0.5, rely=0.85, relwidth=0.15, relheight=0.08)
    # b6 = Button(top, text="Exit", bg='red', fg='black',
    #             activebackground="#FBB195", font=('Courier New', 15), command=top.destroy)
    # b6.place(relx=0.5, rely=0.85, relwidth=0.15, relheight=0.08)

    top.mainloop()


root = Tk()
root.geometry("1500x800")
root.minsize(width=1500, height=800)
root.maxsize(width=1500, height=800)

image = Image.open("out.jpg")
image = image.resize((1500, 800), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(image)
photo_label = Label(root, image=photo1)
photo_label.grid()
    

f1 = Frame(root, bg="#FFBB00", bd=5)
f1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.16)
Label(f1, text="Welcome to Programmer`s library", fg="#FFBB00", bg="black",
      font=('Algerian', 40), padx=50, pady=20).place(relx=0, rely=0, relwidth=1, relheight=1)

b1 = Button(root, text="Log in", bg='black', fg='#FF6700',
            activebackground="#FBB195", font=('Courier New', 20), command=login)
b1.place(relx=0.1, rely=0.35, relwidth=0.3, relheight=0.1)

root.mainloop()