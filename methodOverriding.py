# method overriding is a way of changing the method that is inharited from the base class
class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x*self.y
    

class Circle(Shape):
    def __init__(self,redius):
        self.redius=redius

    def area(self):
        return 3.14*self.redius*self.redius
rec=Shape(23,45)
print(rec.area())
c =Circle(5)
print(c.area())