import numpy as np
'''
trivally easy to calculate for continuous functions

eg 
what is the limite as 'x' approaches 5 in the expression x^2+2x+2?
    in this we ask what is the value of "y" as x approches 5??

same function in python code
'''
def continuous1(x):
    return x**2+(2*x)+2

print(continuous1(5))

'''
for non-continuous functions

lim   x^2-1
     -------
x->1   x-1

but the limition is we cannot pass 1 in the value of x because it will give 0 in the 
denominater and it can't be compute 

for computing for the value for 1 ve can pass the value that is extermly close to the 
1 but not exatly 1 

python code for the silmiler function 

'''
def y_fnx(x):
    return (x**2-1)/(x-1)

print(y_fnx(1.0000001))

'''
lim   sin(x)
     --------
x->0    x

but the limition is we cannot pass 1 in the value of x because it will give 0 in the 
denominater and it can't be compute 

for computing for the value for 1 ve can pass the value that is extermly close to the 
1 but not exatly 1 

python code for the silmiler function
'''
def sin_funx(x):
    return np.sin(x)/x

print(sin_funx(0.00001))

'''
lim           25
            ------
x->infinity   x
'''

def inf_fnx(x):
    return 25/x

print(inf_fnx(0.000001))
