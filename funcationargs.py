#default arguments =if the value is not provided when the funcation is call 
#it will take the argument given while craeting the funcation

def avg(a=3,b=5):
    av=(a+b)/2
    return av
c=avg(b=3)#to send the argument of only one variable
print(c)

#while calling if we want that order dos't matter we call them in key value pair
# it is called keyword funcation
print(avg(b=4,a=8)) 

# required args=the arguments that are required to excute the funcation 

def add(a,b):
    c=a+b
    return c

print(add(23,5)) 

#if we want to pass the tuple to the funcation we pass like this with star"*"

def avg1(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum+=i
    return sum/len(numbers)
print(avg1(34,56,2,7,43))

#if we want to pass arguments as dict

def intro(**names):
    print(type(names))
    print("name=",names["fname"],names["mname"],names["lname"])

print(intro(fname="ram",mname="er",lname="kar"))