from copy import deepcopy
import copy
from my_module import greet, add_number, my_variable
print(greet(10))
print(add_number([1, 2, 3, 4], [10, 20, 30]))
print(my_variable)


def decor(func):
    def wrapper(*args, **kwargs):
        print("before function called")
        result = func(*args, **kwargs)
        print("after function called")
    return wrapper


@decor
def add(a, b):
    return a+b


result = add(10, 20)
print(result)


def log_details(func):
    def wrapper(*args, **kwargs):
        print(
            f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(result)
        print(f"Function '{func.__name__}' executed with result: {result}")
        return result
    return wrapper


@log_details
def add(a, b):
    return a + b


add(2, 3)


def modified_func(func):
    def wrapper():
        print("before function is called")
        func()
        print("after function is called")
    return wrapper


@modified_func
def index_func():
    print("hello index function reponse")


index_func()

ls1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in ls1:
    print(i, end=" ")

my_number = iter([1, 2, 3, 4, 5, 6])
print(next(my_number))
print(next(my_number))


def func():
    yield 10+20


data = func()
print(next(data))
print(next(data))


def gen_func(num):
    ls2 = []
    for i in num:
        sum = i+1
        ls2.append(sum)
    yield ls2


ls1 = [1, 2, 3, 4, 5]
call = gen_func(ls1)


def func_gen():
    yield 1
    yield 2
    yield 3


obj = func_gen()
print(next(obj))
print(next(obj))
print(next(obj))


def gen_fun1():
    for i in range(1, 100):
        data = i**i
    yield data


fun_call = gen_fun1()
print(next(fun_call))
print(next(fun_call))


def add_func(func):
    def wrapper(*args, **kwargs):
        print(f"this is before calling function")
        value = func(10, 20)
        print(value)
        print(f"this is after calling a function")
    return wrapper


@add_func
def func(a, b):
    return a+b


call_func = func(10, 20)


original_list = [1, [2, 3], 4]
copy_list = copy.copy(original_list)
print(copy_list)
copy_list[1][0] = 1000
print(copy_list)
print(original_list)

ls1 = [1, 2, 3, 4, 5, [10, 20, 30]]
ls2 = copy.copy(ls1)
print(ls2 is ls2)
print(ls2)
ls2[5][1] = 20000
print(ls1)
print(ls2)

ls1 = [1, 2, 3, 4, 5, 6, [1000, 2000, 3000]]
ls2 = ls1.copy()
ls2[6][1] = "X"
print(ls1)
print(ls2)

ls1 = [1, 2, 3, 4, 5, [100, 200, 300]]
ls2 = deepcopy(ls1)
ls2[5][1] = "YYYY"
print(ls1)
print(ls2)
