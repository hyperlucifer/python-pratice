# list is ordered collection of elements of different datatypes in one entity / name
# list is a datatype in python
# when we want to put multiple values under one name then we make list
# list items are seperated by comas and enclosed by square brackets
# list are changable we can add or delete the item
# tuple cannot be change but list can

marks=[23,54,6,"sheth",True]

print(marks)

print(marks[0])

# if in queation there is griven,, then convert them into positive index
# to predict the output
# eg 
print(marks[-3]) 
print(marks[len(marks)-3]) # this is the formula

# to check weather the element is present in the list we use 

if 6 in marks:
    print("true")
else:
    print("false")

if "h" in "sheth": #to check if the given characters are present in the given string
    print("true")

# to print the whole string 
print(marks)
print(marks[:])#prints the whole string
print(marks[1:])#prints from given index till the given index

print(marks[1:5:2])#by giving the jump index it will skip a value while printing

# list comprehension means creating a list on the fly
lst=[i for i in range(4)]  
lst=[i for i in range(4) if i%2==0]  
print(lst)