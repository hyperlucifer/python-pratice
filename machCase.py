#match case is samiller as switch case in python
#there is no need of break statement in python
#it sees if the variable matches the pattern in the given case

x=int(input("enter the number \n"))

match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _ if x!=90:             #we can give multiple default cases like this
        print(x,"is not 90") 
    case _ if x!=80:
        print(x,"is not 80")
    case _ :
        print(x)