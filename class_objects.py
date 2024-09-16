class person:
    Name=""
    opi=""
    salary=None
    def accept(self): #self keyword refers to the current object or class same as this keyword
        self.name=input("enter the person name \n")
        self.opi=input("enter the person opi \n")
        self.salary=int(input("enter the person salary \n"))
    def dispay(self):
        print(f"name is {self.name}")
        print(f"opi is {self.opi}")
        print(f"salary is {self.salary}")

a=person()
a.accept()
a.dispay()