from tkinter import *
from PIL import Image, ImageTk
from bookview import *
top = Tk()
top.geometry("1500x800")
top.minsize(width=1500, height=800)
top.maxsize(width=1500, height=800)

image = Image.open("lib.jpg")
image = image.resize((1500, 800), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
photo_label = Label(top, image=photo)
photo_label.grid()


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
