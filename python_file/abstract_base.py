
from abc import abstractmethod, ABC


class Shape(ABC):
    @abstractmethod
    def area():
        pass

    @abstractmethod
    def parameter():
        pass


class Circle(Shape):
    a = 10

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.a

    def parameter(self):
        return 2*3.14*self.radius


obj1 = Circle(100)
print(obj1.area())


class Meta(type):
    def __new__(cls, name, bases, dct):
        print("Creating class:", name)
        return super().__new__(cls, name, bases, dct)


class Person(metaclass=Meta):
    pass


obj1 = Person()


class Custom_Meta(type):
    def __new__(cls, name, bases, dct):
        print("this is meta class", name)
        return super().__new__(cls, name, bases, dct)


class Customer(metaclass=Custom_Meta):
    pass


obj1 = Customer()


class MyClass:
    def __new__(cls, *args, **kwargs):
        print("creating a new Instance")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("intailizing the instance")
        self.value = value


obj1 = MyClass(10)
print(obj1.value)


class CustomAbstract(ABC):
    @abstractmethod
    def index():
        print("abstract method")

    def demo():
        print("this is demo method")


class Person(CustomAbstract):
    def index():
        pass

    def demo():
        print("person demo class")


obj1 = Person
print(obj1.demo())


def func(*args):
    for i in args:
        print(f"Total Three Value{i}")


closure = func(1, 2, 3, 4, 5, 6, 7)


def func1(**kwargs):
    for k, v in kwargs.items():
        print(f"First Object key and Value-{k}:{v}")


closure1 = func1(name="shrikant", age=26)

a = 10
print(type(a))

ls1 = [1, 2, 3, 4, 5, 5]
print(type(ls1))


class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")


class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def make_sound(self):
        super().make_sound()
        print("Woof")


obj1 = Dog("jacky", "Golden_Retriver")
print(obj1.make_sound())
