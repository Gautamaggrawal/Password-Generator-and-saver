from Tkinter import *
import tkMessageBox
#from shelvepass import *
import shelve
from function import funsearch

class MyDialog:
    def __init__(self, parent):

        top = self.top = Toplevel(parent)
        top.title("Verify")
        top.configure(background='black')

        Label(top, text="Enter your Username for verification!",font="Times 20 bold ",fg='white',bg='black').grid(row=0,column=0)
        

        self.e = Entry(top)
        self.e.grid(row=1,column=0)

        b = Button(top, text="OK", command=self.ok,fg='white',bg='black',font='times 12 bold')
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
        Label(choice,text="Archive saver",font="bold").grid(row=0,column=0)
        Label(choice,text="Archive Name: ").grid(row=1,column=0)
        Ar=Entry(choice)
        Ar.grid(row=1,column=1)
        Label(choice,text="Archive Password: ").grid(row=2,column=0)
        Arp= Entry(choice,show='*')
        Arp.grid(row=2,column=1)

        def run():
            ar=Ar.get()
            arp=Arp.get()
            if ar=="" or arp=="":
                tkMessageBox.showwarning("Message","one of your field is empty")
            else:
                global me
                #from project import user
                #print ("global shelve",me)
                f=shelve.open(me+'.dat')
                x={}
                x.update({ar:arp})
                f['Archive']=x
                f.sync()
                f.close()
                tkMessageBox.showinfo("Congo","Saved!!!")
                choice.destroy()
        Button(choice,text="Save",command=run).grid(row=3,column=1)
        choice.mainloop()
#=============================================================================================================
    elif v.get()==3:
        choice=Tk()
        choice.title("Credit Card")
        choice.geometry("300x300")
        Label(choice,text="Credit Card",font="bold").grid(row=0,column=0)
        Label(choice,text="Enter your Title: ").grid(row=1,column=0)
        title=Entry(choice)
        title.grid(row=1,column=1)
        Label(choice,text="Valid from: ").grid(row=2,column=0)
        Valid=Entry(choice)
        Valid.grid(row=2,column=1)
        Label(choice,text="Valid thru: ").grid(row=3,column=0)
        thru= Entry(choice)
        thru.grid(row=3,column=1)
        Label(choice,text="Card Name: ").grid(row=4,column=0)
        name= Entry(choice)
        name.grid(row=4,column=1)

        def run():
            if title.get()=="" or Valid.get()=="" or thru.get()=="" or name.get()=="":
                tkMessageBox.showwarning("Message","one of your field is empty")
            else:

                #insert(title.get(),valid.get(),"Credit cards")
                global me
                #print ("global shelve",me)
                f=shelve.open(me+'.dat')
                x={}
                y=[Valid.get(),thru.get(),name.get()]
                x.update({title.get():y})
                f['Credit Card']=x
                f.sync()
                f.close()
                tkMessageBox.showinfo("Congo","Saved!!!")
                choice.destroy()
        Button(choice,text="Save",command=run).grid(row=5,column=1)
        choice.mainloop()
#=================================================================
    elif v.get()==2:
        choice=Tk()
        choice.title("Computer Logins")
        choice.geometry("300x300")
        Label(choice,text="Computer Logins",font="bold").grid(row=0,column=0)
        Label(choice,text="Computer Name: ").grid(row=1,column=0)
        cn=Entry(choice)
        cn.grid(row=1,column=1)
        Label(choice,text="Username: ").grid(row=2,column=0)
        ucn=Entry(choice)
        ucn.grid(row=2,column=1)
        Label(choice,text="Password: ").grid(row=3,column=0)
        pcn= Entry(choice,show='*')
        pcn.grid(row=3,column=1)

        def run():
            UCN=ucn.get()
            PCN=pcn.get()
            if UCN=="" or PCN=="":
                tkMessageBox.showwarning("Message","one of your field is empty")
            else:
                #insert(UCN,PCN,"Computer Logins")
                global me
                #print ("global shelve",me)
                f=shelve.open(me+'.dat')  
                x={}
                y=[UCN,PCN]
                x.update({cn.get():y})
                f['Computer Logins']=x
                f.sync()
                f.close()
                tkMessageBox.showinfo("Congo","Saved!!!")
                choice.destroy()
        Button(choice,text="Save",command=run).grid(row=4,column=1)
        choice.mainloop()
#========================================================================================================
    elif v.get()==4:
        choice=Tk()
        choice.title("E-banking")
        choice.geometry("300x300")
        Label(choice,text="E-banking",font="bold").grid(row=0,column=0)
        Label(choice,text="Bank Name: ").grid(row=1,column=0)
        bn=Entry(choice)
        bn.grid(row=1,column=1)
        Label(choice,text="Username: ").grid(row=2,column=0)
        bcn=Entry(choice)
        bcn.grid(row=2,column=1)
        Label(choice,text="Password: ").grid(row=3,column=0)
        bcp= Entry(choice,show='*')
        bcp.grid(row=3,column=1)

        def run():
            BCN=bcn.get()
            BCP=bcp.get()
            if BCN=="" or BCP=="" or bn.get()=="":
                tkMessageBox.showwarning("Message","one of your field is empty")
            else:
                #insert(BCN,BCP,"E-bank")
                global me
                #print ("global shelve",me)
                f=shelve.open(me+'.dat')
                x={}
                y=[BCN,BCP]
                x.update({bn.get():y})
                f['E-bank']=x
                f.sync()
                f.close()
                tkMessageBox.showinfo("Congo","Saved!!!")
                choice.destroy()
        Button(choice,text="Save",command=run).grid(row=4,column=1)
        choice.mainloop()
#====================================================================================================
    elif v.get()==5:
        choice=Tk()
        choice.title("E-shops")
        choice.geometry("300x300")
        Label(choice,text="E-shops",font="bold").grid(row=0,column=0)
        Label(choice,text="E-shops Name: ").grid(row=1,column=0)
        en=Entry(choice)
        en.grid(row=1,column=1)
        Label(choice,text="Username: ").grid(row=2,column=0)
        ecn=Entry(choice)
        ecn.grid(row=2,column=1)
        Label(choice,text="Password: ").grid(row=3,column=0)
        ecp= Entry(choice,show='*')
        ecp.grid(row=3,column=1)

        def run():
            ECN=ecn.get()
            ECP=ecp.get()
            if ECN=="" or ECP=="" or en.get()=="":
                tkMessageBox.showwarning("Message","one of your field is empty")
            else:
                #insert(ECN,ECP,"E-shops")
                global me
                #print ("global shelve",me)
                f=shelve.open(me+'.dat')
                x={}
                y=[ECN,ECP]
                x.update({en.get():y})
                f['E-shops']=x
                f.sync()
                f.close()
                tkMessageBox.showinfo("Congo","Saved!!!")
                choice.destroy()
        Button(choice,text="Save",command=run).grid(row=4,column=1)
        choice.mainloop()
#======================================================================================================
    elif v.get()==6:
        choice=Tk()
        choice.title("Socials")
        choice.geometry("300x300")
        Label(choice,text="Socials",font="bold").grid(row=0,column=0)
        Label(choice,text="Social Networking site: ").grid(row=1,column=0)
        sn=Entry(choice)
        sn.grid(row=1,column=1)
        Label(choice,text="Username: ").grid(row=2,column=0)
        scn=Entry(choice)
        scn.grid(row=2,column=1)
        Label(choice,text="Password: ").grid(row=3,column=0)
        scp= Entry(choice,show='*')
        scp.grid(row=3,column=1)

        def run():
            SCN=scn.get()
            SCP=scp.get()
            if SCN=="" or SCP=="" or sn.get()=="":
                tkMessageBox.showwarning("Message","one of your field is empty")
            else:
                #insert(SCN,SCP,"Socials")
                global me
                #print ("global shelve",me)
                f=shelve.open(me+'.dat')
                x={}
                y=[SCN,SCP]
                x.update({sn.get():y})
                f['Socials']=x
                f.sync()
                f.close()
                
                tkMessageBox.showinfo("Congo","Saved!!!")
                choice.destroy()
        Button(choice,text="Save",command=run).grid(row=4,column=1)
        choice.mainloop()
#============================================================================================================        
    elif v.get()==7:
        choice=Tk()
        choice.title("EMAILS")
        choice.geometry("300x300")
        Label(choice,text="EMAILS",font="bold").grid(row=0,column=0)
        Label(choice,text="E-Mailing site Name/URl: ").grid(row=1,column=0)
        mn=Entry(choice)
        mn.grid(row=1,column=1)
        Label(choice,text="Email-id: ").grid(row=2,column=0)
        mcn=Entry(choice)
        mcn.grid(row=2,column=1)
        Label(choice,text="Password: ").grid(row=3,column=0)
        mcp= Entry(choice,show='*')
        mcp.grid(row=3,column=1)

        def run():
            MCN=mcn.get()
            MCP=mcp.get()
            if MCN=="" or MCP=="" or mn.get()=="":
                tkMessageBox.showwarning("Message","one of your field is empty")
            else:
                #insert(MCN,MCP,"E-Mail")
                global me
                #print ("global shelve",me)
                f=shelve.open(me+'.dat')
                x={}
                y=[MCN,MCP]
                x.update({mn.get():y})
                f['E-Mail']=x
                f.sync()
                f.close()
                
                tkMessageBox.showinfo("Congo","Saved!!!")
                choice.destroy()
        Button(choice,text="Save",command=run).grid(row=4,column=1)
        choice.mainloop()


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
cat=Tk()
v=IntVar()
d = MyDialog(cat)
cat.withdraw()
cat.geometry('400x400') 
cat.title("Categories")
cat.wait_window(d.top)
cat.deiconify()
cat.configure(background='black')
global me
Label(cat,text="Categories",font="Times 25 bold ",fg='white',bg='black').grid(row=0,column=0,sticky=W)
Label(cat,text="---------------------------------------------------------------------------",fg='white',bg='black').grid(row=1,column=0,sticky=W)
Radiobutton(cat,text='Archives',variable=v,value=1,command=ShowChoice,font="Times 15 ",fg='white',bg='black').grid(row=2,column=0,sticky=W)
Radiobutton(cat,text='Computer Logins',variable=v,value=2,command=ShowChoice,font="Times 15 ",fg='white',bg='black').grid(row=3,column=0,sticky=W)
Radiobutton(cat,text='Credit card',variable=v,value=3,command=ShowChoice,font="Times 15  ",fg='white',bg='black').grid(row=4,column=0,sticky=W)
Radiobutton(cat,text='E-banking',variable=v,value=4,command=ShowChoice,font="Times 15 ",fg='white',bg='black').grid(row=5,column=0,sticky=W)
Radiobutton(cat,text='e-shops',variable=v,value=5,command=ShowChoice,font="Times 15 ",fg='white',bg='black').grid(row=6,column=0,sticky=W)
Radiobutton(cat,text='Socials',variable=v,value=6,command=ShowChoice,font="Times 15 ",fg='white',bg='black').grid(row=7,column=0,sticky=W)
Radiobutton(cat,text='Email Accounts',variable=v,value=7,command=ShowChoice,font="Times 15 ",fg='white',bg='black').grid(row=8,column=0,sticky=W)
cat.mainloop()
