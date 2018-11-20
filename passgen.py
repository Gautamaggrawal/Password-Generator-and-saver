from Tkinter import *
import random
import string
import tkMessageBox
root=Tk()
root.geometry("300x400")
root.title("Password generator")
Label(root, text="Website: ").grid(row=0, sticky=W)
Label(root, text="Username: ").grid(row=1, sticky=W)
Label(root, text="Password: ").grid(row=2, sticky=W)
Label(root, text="Password Length: ").grid(row=3, sticky=W)
Label(root, text="Allowed Characters: ").grid(row=4, sticky=W)


# Create widgets
website_e = Entry(root, width=30)
username_e = Entry(root, width=30)
password_e = Entry(root, width=30)
len_e = Entry(root, width=3)
website_e.grid(row=0, column=1, sticky=W)
username_e.grid(row=1, column=1, sticky=W)
password_e.grid(row=2, column=1, sticky=W)
len_e.grid(row=3, column=1, sticky=W)
def create():
    w=website_e.get()
    u=username_e.get()
    
    if w=="" or u=="":
        tkMessageBox.showwarning("Warning","One of your Field is empty")
        return
    else:
        tkMessageBox.showinfo("Congo","Password created succesfully")

def gen():
    l=len_e.get()
    l=int(l)
    print("bhai meri lenth"+str(l) +"   ")
    allowed_classes = []
    print("bhai allowed_classes"+str(allow_uppercase.get()))

    if allow_uppercase.get() == 1:
        allowed_classes.append(0)
    if allow_lowercase.get() == 1:
        allowed_classes.append(1)
    if allow_numbers.get() == 1:
        allowed_classes.append(2)
    if allow_special.get() == 1:
        allowed_classes.append(3)
    print(allowed_classes)
    charclass = [string.ascii_uppercase, string.ascii_lowercase, string.digits, '!$%@#']
    pw = ""
    for x in range(l):
        c= int(random.choice(allowed_classes))
        ch = random.choice(charclass[c])
        pw += str(ch)
        password_e.delete(0,END)
        password_e.insert(0, pw)

        

allow_uppercase = IntVar()
allow_lowercase = IntVar()
allow_numbers = IntVar()
allow_special = IntVar()

uppercase_chk = Checkbutton(root, text="Uppercase letters (A-Z)", variable=allow_uppercase,onvalue=1)
lowercase_chk = Checkbutton(root, text="Lowercase letters (a-z)", variable=allow_lowercase,onvalue=1)
numbers_chk = Checkbutton(root, text="Numbers (0-9)", variable=allow_numbers,onvalue=1)
special_chk = Checkbutton(root, text="Special characters (!$%@#)", variable=allow_special,onvalue=1)

uppercase_chk.grid(row=4, column=1, sticky=W)
lowercase_chk.grid(row=5, column=1, sticky=W)
numbers_chk.grid(row=6, column=1, sticky=W)
special_chk.grid(row=7, column=1, sticky=W)

create_btn = Button(root, text="Create",command=create).grid(row=9, column=1,pady=25,padx=20)
generate_btn = Button(root, text="Generate Password",command=gen).grid(row=8, column=1,pady=10)
back_btn = Button(root, text="Back",command=root.destroy).grid(row=8, column=0)
root.mainloop()
