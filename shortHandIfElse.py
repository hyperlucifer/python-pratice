a=330
b=3303
# it is used for short if else condation to make more readable 
print("a") if (a>b) else print("=") if (a==b) else print("b")

#the else is neccery or it will through an error
print("b") if a<b else ""

# we can also asign a value to the variable based on a condition  ,, because it returns a value
c= a if a>b else 5
print(c)

