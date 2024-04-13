from abc import abstractmethod, ABC
import multiprocessing
import threading
from copy import deepcopy


def func_decorator(func):
    def wrapper():
        print("this function is before calling")
        closure = func()
        print("this function after calling")
    return wrapper


@func_decorator
def say_hello():
    print("hello_world")


say_hello()

ls1 = [1, 2, 3, 4, 5, 5, 6]
print(ls1.__dir__())
for i in ls1:
    print(i)

ls2 = [10, 20, 30, 40, 50]
iter_obj = iter(ls2)
val = next(iter_obj)**2
key = next(iter_obj)**3
print(val)
print(key)


def generator_func(ls1):
    for i in ls1:
        val = i**i
        yield val


ls1 = [1, 2, 3, 4, 5, 6]
data = generator_func(ls1)
print(data)
print(next(data))
print(next(data))
print(next(data))

shallow_copy = [1, 2, 3, 4, 5, 6, 7, ['A', 'B', 'C']]
first_copy_obj = shallow_copy.copy()
first_copy_obj[7][1] = "XXXX"
print(shallow_copy)
print(first_copy_obj)

original_obj = [10, 20, 30, 40, ["first", "second"]]
first_obj = deepcopy(original_obj)

first_obj[4][0] = "TEN"
print(original_obj)
print(first_obj)


def print_number():
    for i in range(1, 5):
        print(i)


def print_letters():
    for j in "ABCDE":
        print(j)


thread1 = threading.Thread(target=print_number)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


def square(num):
    return num*num


if __name__ == "__main__":
    number = [1, 2, 3, 4, 5, 6]
    with multiprocessing.Pool() as pool:
        results = list(map(square, number))

    print(number)
    print(results)


def func(x):
    return x**2


def func2(y):
    return y**2+10**10


closure = func(10)
print(closure)
print(func2(closure))


def is_even(x): return x % 2 == 0


for i in range(10):
    print(is_even(i))


def func(num):
    return num*num


number = [1, 11, 111, 1111, 11111]
result = list(map(func, number))
print(result)


class CustomClass(ABC):
    @abstractmethod
    def length():
        pass

    @abstractmethod
    def width():
        pass


class Shape(CustomClass):
    def hello():
        return "hello_world"


obj1 = Shape()
print(obj1)


class IndexClass(type):
    def __new__(cls, name, bases, dct):
        print(f"this is custom meta class", name)
        return super().__new__(cls, name, bases, dct)


class CustomClass(metaclass=IndexClass):
    pass


obj1 = CustomClass()


class MyClass:
    def __new__(cls, *args, **kwargs):
        print("creating a new instance")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        self.value = value
        self.value


obj1 = MyClass(10)
print(obj1.value)


class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Sound generic animal sound")


class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def make_sound(self):
        super().make_sound()
        print("woof")


obj1 = Dog("Jacky", "Goldean")
obj1.make_sound()


class MyClass:
    def add(self, a, b):
        return a, b

    def add(self, a, b, c):
        return a, b, c


obj1 = MyClass()
print(obj1.add(10, 20, 30))


class Animal:
    def make_sound(self):
        print("generic make in sound")


class Dog(Animal):
    def make_sound(self):
        print("woof")


obj1 = Animal()
obj1.make_sound()

obj2 = Dog()
obj2.make_sound()
