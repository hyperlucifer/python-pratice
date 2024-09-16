# tuple are ordered collection of data items , they store multiple items in a single 
# variable ,, they are seprapted by the coma (,) and enclosed by ()ol
# tuples are immuteable (they cannot be change) otherwise they are same as list 

tup=(1,)#if you want to make tuple of only one element then coma (,) is mandtory 
#or it will identify it as a int

print(type(tup))
#if we do sliceing of the tuple it will not change the origanal tuple, but
# make a new tuple and store that value into it
tup2=(12,2,4,6,43,7,34)
tup3=tup2[2:7:3]
print(tup3)

