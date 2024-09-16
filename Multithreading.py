# it is used to do things parallely

import threading
import time
def func(seconds):
    print(f"sleeping for {seconds}")
    time.sleep(seconds)

# this will run one by one
func(4)
func(3)
func(2)
# same code using threading
t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[3])
t3=threading.Thread(target=func,args=[2])

t1.start() # it dose not wait till the function is fully excuted ,,it just start
t2.start() # and throw it into background to excute ,,and procide to next thread
t3.start()

t1.join() # now it will wait until the thread is fully excuted
t2.join()
t3.join()
