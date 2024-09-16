class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def show(self):
        print(f"the name of employee : {self.id} is {self.name}")

class Programmer(Employee):    # here programmer class inharite all the properties of 
                               # employees ,,therefore the class programmer can use all the 
                               # methods and properties of employee ,,but employee cannot use
                               # the properties of programmer  
    def pro_lang(self):
        print("your lang is python")

e=Employee(2,"sheth")
e.show()
p2=Programmer(3,"der")
p2.pro_lang()