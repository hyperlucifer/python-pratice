# it helps to do many operations of operating system
# it is a builtin module used to automate the things we do in os mannuly
import os

# this is used to make folder

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0,100):
#     os.mkdir(f"data/python{i+1}")

# it is used to rename the folder it takes the source and destination
# for i in range(0,100):
#     os.rename(f"data/python{i+1}",f"data/sheth ch python{i+1}")

# to check which folders is present in the perticular folder

# folder =os.listdir("data")

# for fo in folder:
#     print(fo)
# print(os.getcwd())
for i in range(1,101):
    os.removedirs(f"data/sheth ch python{i}")