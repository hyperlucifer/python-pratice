class maths:
    def __init__(self,num) -> None:
        self.num=num

    def addTONum(self,n):
        self.num=self.num+n

    @staticmethod #static methods belongs to the class not the object of the class 
    def add(a,b): # therefore they donot need to access the instance of the class "self" 
        return a+b # is not needed
    
a=maths(4)
print(a.num)
print(a.add(23,45)) # we can call static method using instance or
print(maths.add(23,45)) # class name