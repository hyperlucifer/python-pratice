# if somehow the pointer is not able to enter inside the loop 
# or loop condation becomes false then it will excute the else statement

for i in range(5):# here the i condition becomes false and not able to enter the loop 
    print(i)  
else:             # then it will enter the else block after printing 0,1,2,3,4
    print("out of bound")

for i in []:
    print(i)

else:
    print("list is empty")

# the else block will only excute when loop is fully excuted not break

for i in range(9):
    print(i)
    if(i==5):
        break
else:
    print("break statement")