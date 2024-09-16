# getters in python are the methods that are used to access the values
# of an object's properties
# they are used to return the value of a specific property and are typically defined using a 
# @property decorator.

class Myclass:
    def __init__(self,value):
        self._value=value
    
    def show(self):
        print(f"Value is {self._value}")
    
    #it is a method that behave like a property
    @property
    def ten_value(self):
        return 10*self._value
    
    # it is important to note that the getter do not take any parameters and we cannot set 
    # the value through getter method 
    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/10

obj = Myclass(10)
obj.ten_value=32
print(obj.ten_value)
obj.show()