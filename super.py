# # in python super keyword refer to the parent class 
# # if we want to call any parent class method from its child class we use super
# # eg 
# class Pclass:
#     def parent_method(self):
#         print("this is paraent class method")

# class Cclass(Pclass):
#     # if there are methods by the same name as the paraent class and we make the object of the 
#     # child class then it will excute the method inside the child class and if we make object of
#     # paraent class it will excute the method written in paraent class
#     #
#     #
#     # but if we want to make method in child class with same name and we want use code writen in 
#     # that base paraent class method with same name then super() method is used
#     def parent_method(self):
#         print("sheth")
#         super().parent_method()
#     def child_method(self):
#         print("this is the child method")
#         super().parent_method()

# pc=Pclass()
# pc.parent_method()
# cc=Cclass()
# cc.parent_method()
# cc.child_method()
#-------------------------------------------------------------------------------------------------
# calling constructor by super keyword
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang

em=Employee(12,"sheth")
em2=programmer(12,"sheth","python")
