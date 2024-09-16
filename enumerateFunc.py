#enumerate funcation is used to get the index and the value in the sequance

marks = [12,43,54,200,45,23,5]
# it will return a tuple by using coma (,) we can unpack the tuple 
for index, mark in enumerate(marks):
    if(index ==3):
        print("sheth chi mark ",mark)
        continue
    print(mark)