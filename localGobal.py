# a variable with some limted scope is called local vaiable like function
# we cannot access the local variable outside its scope

# a variable that is declared outside the function and can be used inside 
# any funcation ,,if the funcation with the same name dose'nt exist in the function
# it is called gobal variable

# we cant change gobal variable using local variable because they both work differently
# the local variable get distroy as soon as the function is finish excuting

x=5
print(f"the gobal variable befour calling variable {x}")

def change():
    global x # now it will consider x from the gobal space and we can now change it
    x=78
    y=67
    print(f"the local varable {x}")

change()

print(f"the gobal variable after calling variable {x}")
#print(y) it will cause the error because y is local variable unaccessable