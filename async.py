# it is used to do asyncronuce programming in python
import asyncio

async def func1():
    await asyncio.sleep(1) 
    print("func1")   
async def func2():
    await asyncio.sleep(1) 
    print("func2")   
async def func3():
    await asyncio.sleep(3) 
    print("func3")   

async def main():
    task=asyncio.create_task(func2()) #this function will run when ever
                                      # it gets free time or free recources
    await func1() # await means waite till that function is fully excuted
    await func3() # this syntax will run function one by one

async def main2():
    l=await asyncio.gather( #this will run function parraly
        func1(),
        func2(),
        func3()
    )
asyncio.run(main())    
