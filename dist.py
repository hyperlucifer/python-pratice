# in python dictnary are ordered collection of data items with key value pair 
# we can create our own index in it

info={'name':'sheth','age':2}
print(info) 
print(info['age']) 
# print(info['age1']) # if we want out program to through error when a key dose'nt exist
print(info.get('age2')) # this will not through an error

print(info.keys())
for key in info.keys():
    print(key,"\n")