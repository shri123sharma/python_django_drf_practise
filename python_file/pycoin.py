
from abc import abstractmethod, ABC
from abc import ABC, abstractmethod
import asyncio
import multiprocessing.pool
import multiprocessing
import time
import threading
from copy import deepcopy
import numpy as np


def main():
    print("This code will only run if the script is executed directly.")


if __name__ == "__main__":
    main()

# this is 1d array
arr1 = np.array([1, 2, 3, 5, 6])
print(type(arr1))
print(arr1)

# this is 2D Array
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(type(arr2))
print(arr2)


class Myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_data(self):
        return f"this is data for {self.name}-{self.age}"


obj1 = Myclass('shri', 13)
print(obj1.show_data())


def decorator_func(func):
    def wrapper(*args, **kwargs):
        sum = 0
        for i in args[0]:
            sum += i
        result = func(args[0])
        print(result)
        print(sum)
    return wrapper


@decorator_func
def say_hello(num):
    return "this is sum function print statement"


if __name__ == "__main__":
    num = [10, 20, 30, 40]
    result = say_hello(num)


def generator_func():
    ls1 = []
    for i in range(0, 10):
        ls1.append(i**i)
    yield ls1


if __name__ == "__main__":
    result = generator_func()
    print(next(result))

ls1 = [1, 2, 3, [4, 5, 6]]
ls2 = ls1.copy()
print(id(ls1))
print(id(ls2))

ls2[3][2] = "X"
print(ls2)
print(ls1)

ls1 = ["ANB", "BNF", ["CVB", "DFG"]]
ls2 = deepcopy(ls1)
print(ls2)
print(ls1)

ls2[2][0] = "100000"
print(ls2)
print(ls1)


def print_number():
    for i in range(5):
        print(i)
        time.sleep(1)


def print_letters():
    for k in "ABCDE":
        print(k)
        time.sleep(1)


thread1 = threading.Thread(target=print_number)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


def square(num):
    return num*num


if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = list(map(square, number))
        print(type(result))


def outer_func(x):
    def inner_func(y):
        return x+y
    return inner_func


closure = outer_func(10)
print(closure(6))


def is_even(x): return x % 2 == 0


for i in range(10):
    print(is_even(i))


def func_map(num):
    if num % 2 == 0:
        return "Even number"


if __name__ == "__main__":
    number = [1, 2, 3, 4, 5, 6]
    result = list(map(func_map, number))
    print(result)


def func_filter(num):
    if num % 2 == 0:
        return "Even number"


if __name__ == "__main__":
    number = [1, 2, 3, 4]
    result = list(filter(func_filter, number))
    print(result)


class Car:
    def __init__(self):
        pass

    def say_hello(self, value_list):
        self.value = value_list
        sum = 0
        for i in self.value:
            sum += i
        return sum


obj1 = Car()
print(obj1.say_hello([1, 2, 3, 4, 5, 6, 7, 8, 9]))


class Shape(ABC):
    @abstractmethod
    def area():
        pass

    @abstractmethod
    def parameter():
        pass


class Circle(Shape):
    a = 10

    def area():
        return 10*20

    def parameter():
        return 100*200


obj1 = Circle()
print(obj1.area)


class Shape(ABC):
    @abstractmethod
    def area():
        pass

    @abstractmethod
    def parameter():
        pass


class Circle(Shape):
    a = 10

    def __init__(self, value):
        self.value = value

    def area(self):
        return 3.14*self.value*self.a

    def parameter(self):
        return 3.14*2*self.value


obj1 = Circle(100)
print(obj1.area())


class MyMeta(type):
    def __new__(cls, bases, name, dct):
        dct['cutsom_attribute'] = "this is custom attribute is called"
        return super().__new__(cls, bases, name, dct)


class MyClass(metaclass=MyMeta):
    pass


obj1 = MyClass()
print(obj1.__dict__)


class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print("Creating class:", name)
        dct['custom_attribute'] = 'This is a custom attribute'
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
    pass


print(MyClass.custom_attribute)


class Myclass:
    def __new__(cls, *args, **kwargs):
        print("this is creatig new instance")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("this is intilaizin instance")
        self.value = value


obj1 = Myclass(10)
print(obj1.value)


class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"


class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        return "Dog is broke"


obj1 = Dog("pitbull")
print(obj1.make_sound())


class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "this is animal make sound"


class Dog(Animal):
    def __init__(self, breed):
        self.breed = breed

    def make_sound(self):
        return "make sound is dog lavrador"


obj1 = Animal("dark_species")
print(obj1.make_sound())

obj2 = Dog("pitbull")
print(obj2.make_sound())


class MyClass:
    a = 10

    def __init__(self, b):
        self.b = b

    def add(self):
        return self.a+self.b


obj1 = MyClass(300)
print(obj1.add())


class Myclass:
    a = 10
    b = 20

    def __init__(self, c):
        self.c = c

    @classmethod
    def add(cls, *args, **kwargs):
        return cls.a+cls.b


obj1 = Myclass(30)
print(obj1.add())


def task1():
    print("task1 is started")
    time.sleep(3)
    print("task1 is completd")


def task2():
    print("task2 is started")
    time.sleep(3)
    print("task2 is completed")


if __name__ == "__main__":
    start_time = time.time()
    task1()
    task2()
    end_time = time.time()
    total_time = end_time-start_time
    print(f"Total time to completed two task:-{total_time}")


async def task1():
    print("task1 is started")
    await asyncio.sleep(3)
    print("task1 is completed")


async def task2():
    print("task2 is started")
    await asyncio.sleep(10)
    print("task2 is completed")


async def main():
    start_time = time.time()
    await asyncio.gather(task1(), task2())
    end_time = time.time()
    total_time = end_time-start_time
    print(f"Total time taken in asynorous task:-{total_time}")

if __name__ == "__main__":
    asyncio.run(main())
