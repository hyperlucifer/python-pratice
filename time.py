import time

a=int(time.strftime('%H'))
print(type(a))
if(a>=5&a<12):
    print("good morning")
elif(a>12&a<=15):
    print("good afternoon")
elif(a>15&a<20):
    print("good evening")
else:
    print("good night")

