# single inharitance = when a class inherits properties and behaviours from a single paraent 
#                      class

class Animal:
    def __init__(self,name,sepcies):
        self.name=name
        self.sepcies=sepcies
    def make_sound(self):
        print("sound made by the animal ")

class dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, sepcies="dog")
        self.breed=breed

    def make_sound(self):
        print("Bark!")

d=dog("dog","vodafone")
d.make_sound()
a=Animal("dog","dog")
a.make_sound()