import shelve
from mylibhash import *
def insert(username,password,account):
        f=shelve.open("gautam.dat")
        password=hash_password(password)
        x={}
        x.update({username:password})
        f[account]=x
        f.sync()
        f.close()

def search(username,password,account):
        f = shelve.open("gautam.dat")
        if account in f:
                k=f[account]
                print("F[CREATE ACCOUNT] IS HAVING:")
                for i,j in k.iteritems():
                        if i==username and check_password(j,password):
                                return True
                        else:
                                return False
        f.close()
