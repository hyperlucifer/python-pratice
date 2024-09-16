# in multipleInharitance there are more then one base class for one child class

class Employee:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(f"the name is {self.name}")
class Dancer:
    def __init__(self,dancer):
        self.dancer=dancer
    def show(self):
        print(f"the dance is {self.dancer}")
class DancerEmployee(Employee,Dancer):
    def __init__(self,dancer,name):
        self.dancer=dancer
        self.name=name

# if there are function with same name in both the base clases 
# then it will call the function of the class that is firstly writen in this case Employee

o=DancerEmployee("sheth cha dance","sheth ch nav")

o.show()
print(DancerEmployee.mro())# method rejalucation order (it tells us where is
#                           method is being first)