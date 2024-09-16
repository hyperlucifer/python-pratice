# it is used to handle the error and stop the program from termineting
# for this we use try except

# we think that this line can through an error then we put it ,,
# into the try block and what to do when that error occurs 
# we put it into the expect block

# there are 3 types of errors 
# 1)syntax
# 2)logical
# 3)run time
# it is used to handel runtime error

# a =input("enter the number ")
# print(f"the multiplication table of {a} is \n")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} x {i} = {int(a)*i}")
# except Exception as e:
#     print("wrong input ")
# print ("next code")

# we can also handel multiple types of specific expection 
# by using multiple expection blocks 

try:
    a=int(input("enter the integer"))
    b=[12,67]
    print(b[a])
except ValueError:
    print("the number entered is not integer")
except IndexError:
    print("index error")