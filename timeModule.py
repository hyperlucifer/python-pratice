import time

init=time.time() # it will return the time from when the python is built
def usingWhile():
    i=0
    while(i<=5000):
        print(i)
        i+=1

def usingFor():
    for i in range(5001):
        print(i)
        

usingWhile()
w=init-time.time() # it will return the time from which the code is running  
init=time.time() 
usingFor()
print(init-time.time()) # it will return the time from which the code is running  
print(w)