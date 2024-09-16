class person:
    def __init__(self,na,sal):
        self.name=na
        self.salary=sal

    def info(self):
        print(f"{self.name} is {self.salary}")

a=person("sheth",109090)
b=person("nana",0)
a.info()
b.info()