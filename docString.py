# docString helps us to understand a function/class defination properly 
# docString is not ingonar by the interpretar
# it can be used by giving '''  '''
# by changing the doc it can change the function 
# it writen above the funcation defination

def square(n):
    '''takes a number and writtens the square of it'''
    return n**2
print(square(3))
print(square.__doc__)