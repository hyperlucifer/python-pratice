# classes are the way to define custom datatype
# class method is the type of method that is bound to the class not the instance/object

class Employee:
    company_name="samsung"
    def __init__(self,name) -> None:
        self.name=name
    def show(self):
        print(f"the name is {self.name} and the company name is {self.company_name}")

# we use class method to edit the class 
    @classmethod
    def changeCom(cls,newcom): # the first argument it takes is the class name not the instance 
        cls.company_name=newcom # like a normal method

e1=Employee("nana")
e1.show()
e1.changeCom("dell")
e1.show()
