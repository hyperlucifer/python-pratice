l=[4,23,8,3,1]
print(l)
l.append(65)# adds the value at the end of the list
print(l)
#l.sort(reverse=True)#sort the list in reverce order
#l.reverse()#reverce the list
print(l.index(3))#gives the index of element in the list
print(l.count(3))#gives the count of the given indexin the list
m=l.copy()# copies l list into m list
l.insert(1,32)# it inserts the value in the given index
o=[9,78,65]
l.extend(o) # it will put all the elements of list o and put them into end of the list l
k=l+m  # it will concatnate 2 lists and add them into new list without changing that 2 lists 
print(l)
print(k)