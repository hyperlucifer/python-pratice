# the methods that starts and ends with double underScore are called magic or dunder methods

class Employee:
    name="sheth"
    def __len__(self):
        return len(self.name)
e=Employee()

print(e.name)
print(len(e))