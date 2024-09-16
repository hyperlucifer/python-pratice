# fString is used to formating string
# it used to put the value inside the '{}' brackets
# this is an old way  

a="aapli {} ,,aapli {}"
f=a.format("mati","mansa") # it insert the values respectivly or by giving the index
print(f)

ind="My name is {1} main duniya main {0} hu" # we are pass the index like this from 0
i = ind.format("aakela","anthony gonsarvis")
print(i)
#new way
#by using fString we can insert variables inside the string

name="india"
count="country"
result=f" {name} is my {count}"# "f" in the staring of the string is compalsary           
print(result)
var=f" {{name}} is my {{count}}"# to display the variable name as it is we use
                                             # double curly brackets {{}}
print(var)