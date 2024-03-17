class Car:
    pass

    def add(self):
        return 10+20


obj1 = Car()
print(obj1.add())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def default_information(self, location):
        self.location = location
        return f"Person information is {self.name}-{self.age}-{self.location}"


obj1 = Person("User1", 23)
print(obj1.default_information("indore"))

# my_package/
#     __init__.py
#     module1.py
#     module2.py
