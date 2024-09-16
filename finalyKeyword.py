# finaly block will always excute irrespective of wheather error occer or not
# it can be also use instead of expect block 
# try:
#     l=[5,3,6,2]
#     i=int(input("enter the index\n"))
#     print(l[i])
# except:
#     print("some error occurred \n")
# finally:
#     print("i am always excuted \n")
# what is the difference of using finally and not because both will excute similary
    # the difference came when we use same code function 
# print("i am also always excuted ")
# eg
def fi():
    try:
        l=[5,3,6,2]
        i=int(input("enter the index\n"))
        print(l[i])
        return 1
    except:
        print("some error occurred \n")
        return 0
    finally:
        print("i am in finally ")
    # now it will not excute unless we use finally
    print("i am always excuted \n")
x=fi()
print(x)