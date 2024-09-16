# it is used when a function runs for a same value multiply times 
# when a funcation is called then it rememberes it's retuned value and when it is again called 
# it will return the remembered value insted of excuting the function again ,, it will speed of
# the program
# it is used by importing functools

import functools
import time

@functools.lru_cache(maxsize=None)

def dx(n):
    time.sleep(5)
    return n*5

print(dx(20))
print("done for 20")
print(dx(2))
print("done for 2")
print(dx(30))
print("done for 30")
# it will not run the function below again ,,it will directly return the value direactly from cache  
print(dx(20))
print("done for 20")
print(dx(2))
print("done for 2")
print(dx(30))
print("done for 30")

# use it when you know the function values are limited and are repited multiple times
# because it eats the memory