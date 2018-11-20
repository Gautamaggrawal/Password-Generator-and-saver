import sys
import ttk
import random
import shelve
from Tkinter import *
import Tkinter
import tkMessageBox
import subprocess
from shelvepass import *
from mylibhash import *
from function import fun
root = Tk()
global me
root.configure(background='black')
root.iconbitmap(default='icon.ico')
root.geometry('380x400+30+30')
root.title('Password Generator and Saver')
Label(root,text="Password Generator and Saver",fg='white',bg='black',font='times 20 bold underline').grid()
Label(root,text="Username: ",fg='white',bg='black',font='times 15 bold').grid()
u= Entry(root)  
u.grid()
Label(root,text="Password: ",fg='white',bg='black',font='times 15 bold').grid()
p= Entry(root,show='*')
p.grid()
x=0
y=""

def getup():
    uu=u.get()
    pp=p.get()
    if uu=="admin" and pp=="admin":
        x=1
        y="admin"
        global me
        me=y
        fun(y)
        root.destroy()
        first(x,y)
        #user(y)


    elif search(uu,pp,"Create account")==True:
            x=0
            y=uu
            global me
            me=y
            fun(y)
            root.destroy()
            first(x,y)
            #user(y)
             
    else:
         tkMessageBox.showwarning("Message","Your are not registered or invalid username or password")

def categories():
    subprocess.call("python  projectcat.py")
def savedcat():
    subprocess.call("python  savedcat.py")
def myacc():
    acc=Tk()
    global me
    acc.configure(background="black")
    acc.title("My Account")
    acc.geometry('300x300')
    Label(acc,text=("         Welcome User    "),font="Times 20 bold ",justify='center',fg='white',bg='black').grid(row=0,column=0)
    
    def ask():
        ans=tkMessageBox.askyesnocancel("Confirm!!","Do you really wish to reset your  saved passwords??")
        if ans==True:
            global me
            f=shelve.open(me+".dat")
            f.clear()
            tkMessageBox.showinfo("Info","Data Successfully cleared from Database!!")
        else:
            tkMessageBox.showinfo("Info","Data Not cleared")
    Button(acc,text="RESET",font=" times 15 bold ",command=ask,fg='red',bg='black').place(x=120,y=80)
    Label(acc,text="NOTE:This will delete all your saved Data",fg='red',bg='black',font='times 11 bold').place(x=10,y=200)
    acc.mainloop()

def first(x,y):
    f=Tk()
    f.geometry('400x400+30+30')
    f.title("Welcome")
    f.configure(background='black')
    Label(f,text="Password Generator and Saver",fg='white',bg='black',font='times 20 bold underline').grid()
    Label(f,text="",width=55,fg='white',bg='black').grid()
    if x==1:
        Label(f,text=("Welcome "+y),fg='red',bg='black',font='times 13 bold ').grid()

    else:
        Label(f,text=("Welcome "+y),fg='white',bg='black',font='times 13 bold ').grid() 
    
    def exit():
        a=tkMessageBox.askyesno("Confirm!!","Are you sure to logout?")
        if a==True:
            f.destroy()

    Button(f,text="Categories",width=10,height=3,font="bold ",command=categories,fg='white',bg='black').place(x=50,y=100)
    Button(f,text="My Account",width=10,height=3,font="bold ",command=myacc,fg='white',bg='black').place(x=250,y=100)
    Button(f,text="Show Saved",width=10,height=3,font="bold ",command=savedcat,fg='white',bg='black').place(x=30,y=230)
    Button(f,text="logout",width=4,height=0,font="bold ",command=exit,fg='white',bg='black').place(x=260,y=60)

    def gen():
        subprocess.call("python  passgen.py")
    Button(f,text="Generate password!!",width=18,height=3,font="bold ",command=gen,fg='white',bg='black').place(x=210,y=230)
    f.mainloop()
def message():
    tkMessageBox.showinfo("About", "This software is used to creating passwords,saving the passwords in your pc and manging  passwords of your account.")

#for new user registration
def newuser():
    newu=Tk()
    newu.geometry('400x400+30+30')
    newu.title('Registration')
    Label(newu,text="Create Account").grid()
    Label(newu,text="==================",width=55).grid()
    Label(newu,text="Name: ").grid()
    na=Entry(newu)
    na.grid()
    Label(newu,text="Email: ").grid()
    em=Entry(newu)
    em.grid()
    Label(newu,text="UserId: *").grid()
    u= Entry(newu)
    u.grid()
    Label(newu,text="Password: *").grid()
    p= Entry(newu,show='*')
    p.grid()
    Label(newu,text="Verify Password: *").grid()
    p1= Entry(newu,show='*')
    p1.grid()
    def getnu():
        passw=p.get()
        uu=u.get()
        if p.get()=="" or p1.get()=="" or u.get()=="" or na.get()=="" or em.get()=="":
        	tkMessageBox.showwarning("Warning","One of your field is empty")
        elif p.get()==p1.get():
            f=shelve.open('usernames.txt')
            if uu in f['usernames']:
                tkMessageBox.showerror("ERROR","Couldn't create user already exist!!",icon='error')
                newu.destroy()
            else:
                x=hash_password(passw)
                insert(uu,passw,"Create account")
                tkMessageBox.showinfo("Congo","Registered Successfully!!")
                newu.destroy()
        else:
        	tkMessageBox.showerror("Error","passwords not matched!")            
    Button(newu,text="Create",command=getnu).grid()
    newu.mainloop()

Button(root,text="Login",command=getup,fg='white',bg='black',font='times 12 bold').grid()
Button(root,text="About",command=message,fg='white',bg='black',font='times 12 bold').grid()
Button(root,text="Create account",command=newuser,fg='white',bg='black',font='times 12 bold').grid()
Label(root,text=" ",fg='red',bg='black',font='times 11 bold').grid()
Label(root,text="NOTE:Please take backup after each and every process",fg='red',bg='black',font='times 11 bold').grid()
Label(root,text="This software is free from Sql Injection.",fg='red',bg='black',font='times 11 bold').grid()
Label(root,text="Every Password and Username are cases sensitive",fg='red',bg='black',font='times 11 italic').grid()

root.mainloop()
