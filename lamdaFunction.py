# lamda function is a small anonymous function without a name.
# it is define using lamda keyword 
# in simple words making a variable of a finction ,,and use it as a function

# eg
double = lambda x: x*2 #it will take the value at the left as a argument and it will
                       # perform the operation witten on right side of the function

# it can take multiple values as a argument

print(double(23)) 

# it is generly used for single line function or to pass function as a argument to another func
# eg

def appl (fun,value):
    return fun(value)+ value 

print(appl(lambda x: x*x*x,2))