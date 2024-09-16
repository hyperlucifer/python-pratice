# we use instance variable when we want to asociate a property to a perticular object
# means it is different for every object (eg "name","salary","id")

# and class variable is to make a variable for the class that is to be shared among 
# all the objects/instanceses of that class 
# means it is same for every object (eg "school name","company_name")

class Employee:
    company_name="samsang" #it is a class variable because the company for all employees is same

    def __init__(self,name):
        self.name=name        # it is the instance vaiable because its different for all the objects
        self.raise_amount=0.02
    def show(self):
        print(f"the name of the employee is {self.name} the amount raise in the company {self.company_name} is { self.raise_amount}")

emp1=Employee("nana")
emp1.raise_amount=89
emp1.show()
emp2=Employee("aaba")
emp2.company_name="dell" # here it will change the company name only for emp2,,
                         # original class variable will not be affected 
emp2.show() 

Employee.company_name="apple" #now it will affect the actule class variable 
emp1.show()