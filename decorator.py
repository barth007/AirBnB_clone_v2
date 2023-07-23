#!/usr/bin/python3

"""def my_decorator(func):
    def inwrap():
        print("this is decorator")
        func()
        print("this is decorator")
    return inwrap

@my_decorator
def outside_func():
    print("This is the function")

outside_func()"""

#A function that repeats another funcion

def repeat(num_times):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return my_decorator

@repeat(3)
def call_owners(name):
    print(f"Hello, {name}")

call_owners("Barth")
