# decorators are the functions ,,that accepts a function change it and again return a function
def greet(fx):
    def mfx(*args,**kwargs):# args are use to take arguments as tuple
                            # kwargs are use to take arguments as dist
        print("Good morning")
        fx(*args,**kwargs)
        print("thank you for using this function")
    return mfx

@greet # this tells is that apply the decorator to the function below 
def hello():
    print("sheth cha function")

@greet
def add(a,b):

    print(a+b)

#hello()
add(23,54)