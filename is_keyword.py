# is keyword is used to check if the value's are similar (it is similar as "==" opertor)

# is keyword is used to compare exact location of object in memory 
# == checks the values

a=[2,3,4] 
b=[2,3,4]
# here the list a and b has the same values but different memory address
print(a is b)
print(a == b)

# but here when the value is single and same or any imuteable thing like string or tuple
# therefore it returs true for both the values 
c=4
d=4
print(c is d)
print(c == d)