import multiprocessing
import threading
from copy import deepcopy
from index_class import MyCustomer


def func(a: int, b: int):
    return a+b


result = func(10, 20)
print(result)


def func1(a: int, b: int):
    return a+b


result = func1(10, 20)
print(result)


def countdown(n):
    while n > 0:
        yield n
        n -= 1


# Using the generator
for i in countdown(5):
    print(i)

# Decorator function


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

# Applying the decorator


@my_decorator
def say_hello():
    print("Hello!")


# Calling the decorated function
say_hello()

print("hello_world")


obj1 = MyCustomer("shri", "24", "vijay nagar", "indore")
print(obj1.show_data())


def Decorator_func(func):
    def wrapper():
        print("this is before the func called")
        print(func())
        print("this is after the func called")
    return wrapper


@Decorator_func
def say_hello():
    return "hello_world"


say_hello()

ls1 = [1, 2, 3, 4, 5, 6]
ts1 = (1, 2, 3, 4, 5, 6, 7)
ss1 = {1, 2, 1, 3, 4, 4, 2, 2}
ds1 = {"name": [1, 2, 3, 4, 5], "age": (10, 20, 30, 40, 50)}
str1 = "Shrikant Sharma"

for i in ls1:
    print(i)
for j in ts1:
    print(j)
for k in ss1:
    print(k)
for ls in ds1:
    print(ls)
for m in str1:
    print(m)

ls1_iter = iter(ls1)
print(next(ls1_iter)
      )

ds1_iter = iter(ds1)
print(next(ds1_iter))


def generator_func():
    element_list = []
    for i in range(0, 10):
        multi_value = i**i
        element_list.append(multi_value)
    yield element_list


obj1 = generator_func()
for i in obj1:
    print(i)


ls1 = [1, 2, 3, 4, 4, 5, 6]
ls2 = ls1.copy()
print(ls1)
print(ls2)

ls1_ = [1, 2, 3, 4, [30, 40, 50]]

ls2_ = ls1_.copy()
print(id(ls1_))
print(id(ls2_))

ls2_[4][1] = "G"
print(ls2_)
print(ls1_)

ls1 = [1, 2, 3, 4, 5, [100, 200, 300, 400]]
ls2 = deepcopy(ls1)
print(ls1)
print(ls2)

ls2[5][0] = "YYYYY"
print(ls1)
print(ls2)


def func1():
    for i in range(1, 10):
        print(f"Thread,{i}")


def func2():
    for j in "ABCDE":
        print(f"Thread,{j}")


thread1 = threading.Thread(target=func1)
thread2 = threading.Thread(target=func2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


def square(num):
    return num*num


def addition(num):
    sum_ = 0
    sum_ += num+10
    return sum_


if __name__ == "__main__":
    number = [1, 2, 3, 4, 5.6]
    with multiprocessing.Pool() as pool:
        result1 = list(map(square, number))
        result2 = list(map(addition, number))
    print(result1)
    print(result2)


def outer_func(x):
    def inner_func(y):
        return x+y
    return inner_func


closure = outer_func(10)
print(closure(5))


def result(x, y, z): return x+y+z


print(result(10, 20, 30))
def is_even(x): return x % 2 == 0


print(is_even(11))


def is_even(x): return x % 2 == 0


for i in range(10):
    print(is_even(i))

numbers = [1, 2, 3, 4, 5]


def square(x):
    return x**2


result = map(square, numbers)
print(next(result))
print(next(result))


def func_filter(number):
    if number % 2 == 0:
        return number


if __name__ == "__main__":
    number = [1, 2, 3, 4, 5, 6, 7]
    result = list(filter(func_filter, number))
    print(result)


class Car:
    location = "indore"

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def get_method(self):
        return self.name+"-"+self.brand+"-"+self.location


obj1 = Car("BMW", "TATA")
print(obj1.get_method())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


obj1 = Person()
print(obj1)
