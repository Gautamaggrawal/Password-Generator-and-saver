import shelve
'''f=shelve.open('usernames.txt',writeback=True)
f['usernames']=[]
f.close()'''
def fun(x):
    f=shelve.open('usernames.txt',writeback=True)
    f['usernames'].append(x)
    f.sync()
    f.close()

def funsearch(username):
	f=shelve.open('usernames.txt')
	if username in f['usernames']:
		return True
	else:
		return False



    
