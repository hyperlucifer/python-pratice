#using class method as the alternate for constructors

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    # to handle data from both the formats we use class methods as alt constructor
        
    @classmethod
    def fromStr(cls,str):
        return cls(str.split("-")[0],int(str.split("-")[1]))

e=Employee("nana",12000)

# if we get data as string only then we use string.split method 
# it will return a list of element separeted by the given character
# eg 
str="appa-12300"
e2=Employee.fromStr(str)
print(e2.name)
print(e2.salary)

