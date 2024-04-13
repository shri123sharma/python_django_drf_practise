import multiprocessing
import time
import threading
from copy import deepcopy


class MyClass:
    a = 10

    def __init__(self, x):
        self.x = x

    def instance_method(self):
        return self.x+MyClass.a


print(MyClass(2).instance_method())
obj1 = MyClass(2)
print(obj1.instance_method())


class MyClass:
    a = 10

    def __init__(self, x):
        self.x = x

    @classmethod
    def class_method(cls):
        return cls.a


print(MyClass.class_method())
obj1 = MyClass(100)
print(obj1.class_method())


class MyDevelop:
    class_variable = 100

    def __init__(self):
        self.x = 10
        self.y = 20

    def show_data(self):
        return self.x+self.y+self.class_variable


obj1 = MyDevelop()
print(obj1.show_data())


class Person:
    name = "shrikant"
    age = 26

    def __init__(self, email, phone_number):
        self.email = email
        self.phone = phone_number

    @classmethod
    def class_index_method(cls):
        return cls.name+" "+str(cls.age)


obj1 = Person("shika@gmail.com", 593593893)
print(obj1.class_index_method())
print(Person.class_index_method())


class MyClass:
    class_variable = 10

    def __init__(self, x):
        self.x = x

    @classmethod
    def class_method(cls):
        return cls.class_variable


obj1 = MyClass
print(obj1.class_method())
print(MyClass.class_method())


class Person:
    a = 10
    b = 20

    def __init__(self, key, val):
        self.key = key
        self.val = val

    @staticmethod
    def show_method():
        return "this is static method"+" "+str(Person.a+Person.b*obj1.key*obj1.val)


obj1 = Person(100, 200)
print(obj1.show_method())
print(Person.show_method())


class MyClass:
    @staticmethod
    def static_method():
        return "This is a static method"


print(MyClass.static_method())
obj = MyClass()
print(obj.static_method())


class Customer:
    def __init__(self, value):
        self.value = value

    @property
    def method1(self):
        return self.value

    def method1(self, value):
        self.value = value
        return self.value


obj1 = Customer(100)
print(obj1.method1())
print(obj1.method1(200))


def decorator_func(func):
    def wrapper():
        print("before the function")
        obj1 = func()
        print(obj1)
        print("after the function")
    return wrapper


@decorator_func
def say_hello():
    return "hello world"


say_hello()

ls1 = [1, 2, 3, 4, 5, 6, 6]
for i in ls1:
    print(i)
print(ls1.__dir__())

ls1 = [1, 2, 3, 4, 5, 6]
ls2 = []
for i in range(len(ls1)):
    if i % 2 == 0:
        obj = ls1[i]**2
        ls2.append(obj)
print(ls2)

ts1 = (1, 2, 3, 4, 5, 6)
for i in ts1:
    print(i)

ls1 = [10, 20, 30, 40]
obj1 = ls1.__dir__()
obj2 = ls1.__iter__()
print(next(obj2))
print(next(obj2))


def generator_func():
    ls1 = []
    for i in range(0, 10):
        l1 = i**2
        ls1.append(l1)
    yield ls1


obj1 = generator_func()
print(next(obj1))

ls1 = [1, 2, 3, 4]
ls2 = ls1.copy()
print(id(ls1))
print(id(ls2))
print(ls1 is ls2)

ls1 = [1, 2, 3, 4, 5]
ls2 = ls1.copy()
print(ls1)
print(ls2)
ls2.append(1000)
print(ls2)

ls3 = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
ls4 = ls3.copy()
ls4[3][0] = 5000
print(ls4)
print(ls3)

ls1 = [1, 2, 3, 4]
ls2 = deepcopy(ls1)
print(ls1)
print(ls2)
print(ls1 is ls2)

ls3 = [1, 2, 3, 4, [5, 6, 7], [8, 9, 10]]
ls4 = deepcopy(ls3)
ls4[4][2] = 1000
print(ls3)
print(ls4)


def func1():
    print("func1 is executed")
    time.sleep(3)


def func2():
    print("func2 is executed")
    time.sleep(3)


def func3():
    print("func3 is executed")
    time.sleep(3)


start_time = time.time()  # Record the start time

thread1 = threading.Thread(target=func1)
thread2 = threading.Thread(target=func2)
thread3 = threading.Thread(target=func3)

thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()

end_time = time.time()  # Record the end time

total_time = end_time - start_time
print("Total execution time:", total_time, "seconds")

thread1.join()
thread2.join()
thread3.join()

print("All thread is run")


def func(num):
    return num*num


if __name__ == "__main__":
    number = [1, 23, 4, 5]
    with multiprocessing.Pool() as pool:
        result = list(map(func, number))
        print(result)


def func1():
    return "func1 is call"


def func2():
    return "func2 is call"


def func3():
    return "func3 is call"


def run():
    with multiprocessing.Pool(processes=3) as pool:
        print(pool.map(func1, []))
        print(pool.map(func2, []))
        print(pool.map(func3, []))


if __name__ == "__main__":
    run()


def func(x):
    def wrapper(y):
        return x+y
    return wrapper


closure1 = func(5)
print(closure1.__dir__())
print(closure1(100))


def add(x, y): return x+y


print(add(10, 20))


def add(x, y): return x+y if x > 0 and y > 0 else "Both value is positive"


print(add(2, 3))


def even(num): return num if num % 2 == 0 else "odd number"


number = [1, 2, 3, 4, 5, 6, 7, 8]
for i in number:
    print(even(i))


def sum_func(num):
    print(num)
    return num*num


number = [1, 2, 3, 4, 5, 6, 7]
result = map(sum_func, number)
print(list(result))

number = [1, 2, 3, 4, 5, 6, 7]


def func(num):
    if num % 2 == 0:
        return num
    else:
        return "Odd number"


result = list(map(func, number))
print(result)

number = [1, 2, 3, 4, 5, 6]


def func(num):
    if num % 2 == 0:
        return num


result = list(filter(func, number))
print(result)


class MyPerson:
    location = "indore"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def class_method(cls):
        return cls.location

    @staticmethod
    def static_method():
        return obj1.location+"-"+obj1.name+"-"+str(obj1.age)


obj1 = MyPerson("shrikant", 23)
print(
    f"This instance and class attribute-{obj1.name}-{obj1.age}-{obj1.location}")
print(obj1.class_method())
print(obj1.static_method())


class MyCustomer:
    def __init__(self, name, age, location, city):
        self.name = name
        self.age = age
        self.location = location
        self.city = city

    def show_data(self):
        return super().__init__()


class Book:
    pass


obj1 = Book
print(obj1)
