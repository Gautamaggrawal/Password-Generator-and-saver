from Tkinter import *
import subprocess

def gautam():
    splash.destroy()
    subprocess.call('python project.py')
splash=Tk()
splash.geometry('700x700')
x=PhotoImage(file='se.gif')
Label(splash,text="PASSWORD GENERATER AND SAVER",font='courier 30 bold').place(x=10,y=50)
Label(splash,text="GAUTAM AGGRAWAL",font='courier 25 bold').place(x=50,y=150)
Label(splash,text="161B083",font='courier 25 bold').place(x=50,y=250)
Label(splash,text="Batch:B3",font='courier 25 bold').place(x=50,y=350)
Label(splash,image=x).place(x=450,y=400)
splash.configure(background='black')
splash.title("INTRODUCTION")
splash.after(4000,gautam)
splash.mainloop()