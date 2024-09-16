# generators are a function's that allow you to create alterable sequence of value
# A generator function returns a generator object which can be used to generate the values 
# one-by-one as you iterate over it... 

# it dose not store the value,,but it store the in info from which the value can be made on-the-fly

def my_gen():
    for i in range(5):
        yield i # yield is used to make generators,,it returns the generator and suspends
                # the excution until the next value is requested

# it is used to generate the value as we need and we did'nt have to store the value
# it saves the memory 
# they make value one at a time

gen=my_gen()

print(next(gen))