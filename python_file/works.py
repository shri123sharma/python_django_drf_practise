
from multiprocessing import Process
import threading


def modified_func(func):
    def wrapper():
        print("this is calling to berfore function")
        data = func()
        print("this is calling to after function")
    return wrapper


@modified_func
def say_hello():
    print("hello world")


say_hello()


def print_number():
    for i in range(5):
        print("Thread 1", i)


def print_letter():
    for j in "ABCDE":
        print("Thread 2", j)


# Create threads
thread1 = threading.Thread(target=print_number)
thread2 = threading.Thread(target=print_letter)
# Start threads
thread1.start()
thread2.start()
# Wait for threads to finish
thread1.join()
thread2.join()
print("DONE")


def print_number():
    for i in range(5):
        print("Process 1", i)


def print_letter():
    for j in "ABCDE":
        print("Prcess 2", j)


# create process
process1 = Process(target=print_number)
prcess2 = Process(target=print_letter)
# start process
process1.start()
prcess2.start()
# wait for Process to finish
process1.join()
prcess2.join()


def outer_func(x):
    def inner_func(y):
        return x+y
    return inner_func


closure_method = outer_func(10)
print(closure_method(5))


def third_func():
    return "welcome"


def first_func(func):
    return "hello"


closure = first_func(third_func())


@closure()
def second_func():
    return "world"


second_func()


def is_even(x): return x % 2 == 0


for i in range(5):
    print(is_even(i))

number = [1, 2, 3, 4, 5, 6, 7]


def func(x):
    if x % 2 == 0:
        return "Even Number"


even_number = list(map(func, number))
print(even_number)

number = [1, 2, 3, 4, 5, 6, 7, 8]


def func(x):
    if x % 2 == 0:
        return x


value = list(filter(func, number))
print(value)


class Car:
    cls_var = 10000

    def __init__(index, name, age):
        index.name = name
        index.age = age

    def index(index):
        return f"this is index method parameter {index.name} and {index.age}"


obj1 = Car("shrikant", 23)
obj2 = Car("ajay", 24)
print(obj1.index())
print(obj1.index())
print(Car.cls_var)
print(obj1.cls_var)


class Car:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def default_info(self):
        return f"This is my response {self.name}-{self.age}"


instance_obj1 = Car("shri", 26)
instance_obj2 = Car("ajay", 27)
print(Car)
print(Car)
print(instance_obj1.default_info())
print(instance_obj2.default_info())


class Car:
    def default_info(self):
        return "hello_world"


obj1 = Car()
obj2 = obj1

print(id(obj1))
print(id(obj2))
