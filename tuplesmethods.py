# we cannot change/perform operation on tuples directly we have to convert the tuple 
# into list then perform operation and then convert them again into tuples
# eg

cont=("india","germany","japan","uk","usa")
print(type(cont))
conTemp=list(cont)
print(type(conTemp))
conTemp.pop(cont.index("uk"))
cont=tuple(conTemp)
print(type(cont))
print(cont)

#but we can concatinate them without converting because we are making a a new tuple