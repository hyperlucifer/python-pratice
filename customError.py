# we can make our custom error using raise keyword
# it is used to stop the program if user gives invalid inputs ,,,to avoid father unknow 
# logical or any errors

# a = int(input("enter the number between 9 and 5\n"))

# if (a<5 or a>9):
#     raise ValueError("the number is not between 9 and 5")

a=input("enter the number between 5 and 9\n")

if(a=="quit"):
    print("pass")
elif(int(a)<5 or int(a)>9):
    raise ValueError("the number is not between 5 and 9")
else:
    print("radha")