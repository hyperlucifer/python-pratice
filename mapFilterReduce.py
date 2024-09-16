# # the map function applies a function to each element in a sequence and returns a new list

# def cube(x):
#     return x**3

# l=[2,7,9,6,4]

# newl=list(map(cube,l)) # here the first argument is the function name//it can be lamda function too
#                        # second one is the list to applay function too ,, it is a short cut to apply 
#                        # function too all the elements
# print(newl)

# # filter function filters a sequence of elements based on the given predicate ,,a function that return
# # a boolean value,, and returns a new sequence containing only the element that meets the predicate  

# def fi_func(a):
#     return a>4

# flList=list(filter(fi_func,l))

# print(flList)


# the reduce function is a higher order-function(a function that takes funcation as a argument)
# that applices a function to the sequence and returns a single value 

from functools import reduce

numbers=[1,2,3,4,5,6,7]

sum=reduce(lambda x,y:x+y,numbers) # it will take 2 elements at a time and add them at the end 
                                   # returns the sum of all the elements in list
print (sum)