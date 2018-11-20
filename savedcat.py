import shelve
from Tkinter import *
import tkMessageBox
from function import funsearch
class MyDialog:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.title("Verify")
        top.configure(background='black')
        Label(top, text="Enter your Username for verification!",font="times 20 bold",fg='white',bg='black').grid(row=0,column=0)

        self.e = Entry(top)
        self.e.grid(row=1,column=0)

        b = Button(top, text="OK", command=self.ok,font="times 15 bold",fg='white',bg='black')
        b.grid(row=2,column=0)

    def ok(self):
        x=self.e.get()
        global me
        me=x

        if funsearch(x)==True:
            tkMessageBox.showinfo("Message","Got u!")
            self.top.destroy()
        else:
            tkMessageBox.showwarning("Warning","Not a valid user!!",icon='warning')
          

def ShowChoice():
    print(v.get())
    if v.get()==1:
        choice=Tk()
        choice.title("Archives")
        choice.geometry("300x300")
        Label(choice,text="Archive saver",font=" Times 15 bold").grid(row=0,column=0)
        key='Archive'
        global me
        print("me value:",me)
        f=shelve.open(me+'.dat')
        if key in f:
            k=f[key]
            for i,j in k.iteritems():
                Label(choice,text="Archive Name: ").grid(row=1,column=0,sticky=W)
                Label(choice,text=i,font="bold").grid(row=1,column=1)
                Label(choice,text="Archive password: ").grid(row=2,column=0,sticky=W)
                Label(choice,text=j,font="bold").grid(row=2,column=1)
	f.close()
	choice.mainloop()
#=================================================================================================
    elif v.get()==3:
        choice=Tk()
        choice.title("Credit Card")
        choice.geometry("300x300")
        Label(choice,text="Credit Card",font="Times 15 bold").grid(row=0,column=0)
        global me
        f=shelve.open(me+'.dat')
        if 'Credit Card' in f:
            k=f['Credit Card']
            for i,j in k.iteritems():
                Label(choice,text="Title of your card: ").grid(row=1,column=0,sticky=W)
                Label(choice,text=i,font="bold").grid(row=1,column=1)
                Label(choice,text="Valid from: ").grid(row=2,column=0,sticky=W)
                Label(choice,text=j[0],font="bold").grid(row=2,column=1)
                Label(choice,text="Valid from: ").grid(row=3,column=0,sticky=W)
                Label(choice,text=j[1],font="bold").grid(row=3,column=1)
                Label(choice,text="Valid thru: "+j[2]).grid(row=4,column=0,sticky=W)
                Label(choice,text=j[2],font="bold").grid(row=4,column=1)

        f.close()
        choice.mainloop()
#===============================================================================================
    elif v.get()==2:
        choice=Tk()
        choice.title("Computer Logins")
        choice.geometry("300x300")
        Label(choice,text="Computer Logins",font="Times 15 bold").grid(row=0,column=0)
        global me
        f=shelve.open(me+'.dat')
        if 'Computer Logins' in f:
            k=f['Computer Logins']
            for i,j in k.iteritems():
                Label(choice,text="Computer Name: ").grid(row=1,column=0,sticky=W)
                Label(choice,text=i,font="bold").grid(row=1,column=1)
                Label(choice,text="Username: ").grid(row=2,column=0,sticky=W)
                Label(choice,text=j[0],font="bold").grid(row=2,column=1)
                Label(choice,text="Password: ").grid(row=3,column=0,sticky=W)
                Label(choice,text=j[1],font="bold").grid(row=3,column=1)
        f.close()
        choice.mainloop()
    #============================================================================================
    elif v.get()==4:
        choice=Tk()
        choice.title("E-banking")
        choice.geometry("300x300")
        Label(choice,text="E-banking",font="Times 15 bold").grid(row=0,column=0)
        global me
        f=shelve.open(me+'.dat')
        if 'E-bank' in f:
            k=f['E-bank']
            for i,j in k.iteritems():
                Label(choice,text="Bank Name: ").grid(row=1,column=0,sticky=W)
                Label(choice,text=i,font="bold").grid(row=1,column=1)
                Label(choice,text="Username: ").grid(row=2,column=0,sticky=W)
                Label(choice,text=j[0],font="bold").grid(row=2,column=1)
                Label(choice,text="Password: ").grid(row=3,column=0,sticky=W)
                Label(choice,text=j[1],font="bold").grid(row=3,column=1)
        f.close()
        choice.mainloop()
    #===================================================================================
    elif v.get()==5:
        choice=Tk()
        choice.title("E-shops")
        choice.geometry("400x300")
        Label(choice,text="E-shops",font="Times 15 bold").grid(row=0,column=0)
        global me
        f=shelve.open(me+'.dat')
        if 'E-shops' in f:
            k=f['E-shops']
            for i,j in k.iteritems():
                Label(choice,text="E-shops Name: ").grid(row=1,column=0,sticky=W)
                Label(choice,text=i,font="bold").grid(row=1,column=1)
                Label(choice,text="Username: ").grid(row=2,column=0,sticky=W)
                Label(choice,text=j[0],font="bold").grid(row=2,column=1)
                Label(choice,text="Password: ").grid(row=3,column=0,sticky=W)
                Label(choice,text=j[1],font="bold").grid(row=3,column=1)
        f.close()
        choice.mainloop()
#===============================================================================================
    elif v.get()==6:
        choice=Tk()
        choice.title("Socials")
        choice.geometry("400x300")
        Label(choice,text="Socials",font="Times 15 bold").grid(row=0,column=0)
        global me
        f=shelve.open(me+'.dat')
        if 'Socials' in f:
            k=f['Socials']
            for i,j in k.iteritems():
                Label(choice,text="Socials Site Name: ").grid(row=1,column=0,sticky=W)
                Label(choice,text=i,font="bold").grid(row=1,column=1)
                Label(choice,text="Username: ").grid(row=2,column=0,sticky=W)
                Label(choice,text=j[0],font="bold").grid(row=2,column=1)
                Label(choice,text="Password: ").grid(row=3,column=0,sticky=W)
                Label(choice,text=j[1],font="bold").grid(row=3,column=1)
        f.close()
        choice.mainloop()
    #=============================================================================================
    elif v.get()==7:
        choice=Tk()
        choice.title("EMAILS")
        choice.geometry("400x300")
        Label(choice,text="EMAILS",font="Times 15 bold").grid(row=0,column=0)
        global me
        f=shelve.open(me+'.dat')
        if 'E-Mail' in f:
            k=f['E-Mail']
            for i,j in k.iteritems():
                Label(choice,text="E-Mailing site Name/URl: ").grid(row=1,column=0,sticky=W)
                Label(choice,text=i,font="bold").grid(row=1,column=1)
                Label(choice,text="Username: ").grid(row=2,column=0,sticky=W)
                Label(choice,text=j[0],font="bold").grid(row=2,column=1)
                Label(choice,text="Password: ").grid(row=3,column=0,sticky=W)
                Label(choice,text=j[1],font="bold").grid(row=3,column=1)
        f.close()
        choice.mainloop()
#===============================================================================================        
savedcat=Tk()
d = MyDialog(savedcat)
v=IntVar()
savedcat.configure(background='black')
savedcat.withdraw()
savedcat.geometry('400x400') 
savedcat.title("Categories")
savedcat.wait_window(d.top)
savedcat.deiconify()
global me
Label(savedcat,text="Categories",font="times 25 bold",fg='white',bg='black').grid(row=0,column=0,sticky=W)
Label(savedcat,text="---------------------------------------------------------------------------",fg='white',bg='black').grid(row=1,column=0,sticky=W)
Radiobutton(savedcat,text='Archives',variable=v,value=1,command=ShowChoice,font="Times 15 ",fg='white',bg='black').grid(row=2,column=0,sticky=W)
Radiobutton(savedcat,text='Computer Logins',variable=v,value=2,command=ShowChoice,font="Times 15 ",fg='white',bg='black').grid(row=3,column=0,sticky=W)
Radiobutton(savedcat,text='Credit card',variable=v,value=3,command=ShowChoice,font="Times 15 ",fg='white',bg='black').grid(row=4,column=0,sticky=W)
Radiobutton(savedcat,text='E-banking',variable=v,value=4,command=ShowChoice,font="Times 15 ",fg='white',bg='black').grid(row=5,column=0,sticky=W)
Radiobutton(savedcat,text='e-shops',variable=v,value=5,command=ShowChoice,font="Times 15 ",fg='white',bg='black').grid(row=6,column=0,sticky=W)
Radiobutton(savedcat,text='Socials',variable=v,value=6,command=ShowChoice,font="Times 15 ",fg='white',bg='black').grid(row=7,column=0,sticky=W)
Radiobutton(savedcat,text='Email Accounts',variable=v,value=7,command=ShowChoice,font="Times 15 ",fg='white',bg='black').grid(row=8,column=0,sticky=W)
savedcat.mainloop()

