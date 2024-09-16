#for loop can alterate over a sequence of altarable objects 
x="gfhygb"
for x in x:
    print(x)
    if (x=='b'):
        print("sheth loka")

colors=["red","blue","green","yellow"]

for color in colors:
    print(color)
    for i in color:
        print(i)

# for k in range(5): #range prints the number to n-1
#     print(k)
# for k in range(1,20001): #we can also give starting and ending value tooo
#     print(k)
for k in range(1,21,2): #step is used to modify the output value
    print(k)