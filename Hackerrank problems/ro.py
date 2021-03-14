import time                     

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        f_name = func.__name__
        print("time taken to execute " + f_name + str( (end-start)*1000) + " ms.")
        return result
    return wrapper

@time_it
def square_func(numbers):
    a=[]
    for i in numbers:
        a.append(i*i)
    return a

@time_it
def cube_func(numbers):
    b=[]
    for i in numbers:
        b.append(i*i*i)
    return b

numbers = range(1,1000)
square_func(numbers)
cube_func(numbers)