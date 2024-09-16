# object introsection means you want to know what is present in that object
# and to know about that class 

# there are mainly 3 methods 
# dir(), 
# _dict_ ,help()

# dir = the dir() return a list of all the attributes and methods avaliable for that object
x=[1,2,3]
# print(dir(x))
# print(x.__add__)

# __dict__ atribute = returns a dictionery representing the objects variables of that class
                    # it will only return a instance variable(with "self") not a class variable

class Employee:
    salary=78
    def __init__(self,id,name):
        self.id=id
        self.name=name
    
e=Employee(98,"mh")
print(e.__dict__)

# help() = help functin is used to get help documentation for an object including
# a description of its attributes and methods 

print(help(Employee))