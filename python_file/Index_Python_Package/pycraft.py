# from abc import abstractmethod,ABC
# class Shape(ABC):
#     @abstractmethod
#     def area():
#         pass
#     @abstractmethod
#     def parameter():
#         pass

# class Circle(Shape):
#     def area():
#         pass
#     def parameter():
#         pass

# obj1=Circle()
# print(obj1)

# class Meta(type):
#     def __new__(cls,name,bases,dct):
#         dct["custom_attribute"]="this is custom attribute for this class"
#         return super().__new__(cls,name,bases,dct)

# class Myclass(metaclass=Meta):
#     pass

# print(Myclass.custom_attribute)

# class MyPerson:
#     def __new__(cls,*args):
#         print("New instance is created")
#         instance=super().__new__(cls)
#         return instance

#     def __init__(self,value):
#         print("New instance is intailzing")
#         self.value=value

# obj1=MyPerson(10)
# print(obj1.value)

# def func(key,val):
#     for i in num:
#         print(f"Total value is Three{i}")

# var=func()
# var

# class Animal():
#     def __init__(self,name,breed):
#         self.name=name
#         self.breed=breed

#     def make_sound(self):
#         print("Some generic animal sound")

# class Dog(Animal):
#     def __init__(self,name,breed,species):
#         self.species=species

#     def make_sound(self):
#         super().make_sound()
#         super().__init__(self.name,self.breed)
#         print("Woof")

# obj1=Dog("hello","world","indore")
# obj1.make_sound()

# class Myclass:
#     def add(self,a,b):
#         return a+b

#     def add(self,a,b,c):
#         return a+b+c
# obj1=Myclass()
# print(obj1.add(10,20,30))

# class Animal:
#     def make_sound(self):
#         return "Generic Animal Sound"

# class Dog(Animal):
#     def make_sound(self):
#         return "Woof"

# animal=Animal()
# dog=Dog()

# print(animal.make_sound())
# print(dog.make_sound())

# class MyClass:
#     location="Indore"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def show_data(self):
#         return self.name+str(self.age)+self.location
# obj1=MyClass("shri",25)
# print(obj1.show_data())

# class Person:
#     location="indore"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     @classmethod
#     def class_method(cls):
#         return cls.location

# obj1=Person("shri",34)
# print(obj1.name)
# print(obj1.age)
# print(obj1.class_method())

# class Myclass:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     @staticmethod
#     def static_method():
#         return "this is static method"
# obj1=Myclass("shri",23)
# print(obj1.static_method())

# def divide_func(x,y):
#     try:
#         result= x/y

#     except ZeroDivisionError:
#         print("Error!Division by Zero")

#     except TypeError:
#         print("Error:unsupported operand type(s) for division")

#     except Exception as e:
#         print("An error occured",e)

#     else:
#         print("Result:",result)

#     finally:
#         print("End of Error hanling")
# var=divide_func(10,0)
# var

# class Exception:
#     def divide_value(self,x,y):
#         try:
#             self.x=x
#             self.y=y
#             result=self.x/self.y
#         except ZeroDivisionError:
#             print("Division By Zero")
#         except TypeError:
#             print("Unsupported type error for division")

#         except ArithmeticError:
#             print("Error: Arithmetic error occurred!")

#         else:
#             print("Result",result)
#         finally:
#             print("End of the error handling")
# obj1=Exception()
# obj1.divide_value(10,20)
# obj1.divide_value(10,0)
# obj1.divide_value(10,"0")

# import gc
# class MyPerson:
#     def __init__(self,name):
#         self.name=name
#         print(f"Object is {self.name} Created")
# obj1=MyPerson("First_object")
# obj2=MyPerson("Second_object")

# obj1=obj2
# obj2=obj1

# print(gc.collect())

# import threading

# def count_up(n):
#     for i in range(1,n+1):
#         print(f"Thread-{i}")

# thread1=threading.Thread(target=count_up,args=(5,))
# thread2=threading.Thread(target=count_up,args=(5,))

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# class Myclass:
#     def __init__(self):
#         self.public_arr=10

# obj1=Myclass()
# print(obj1.public_arr)

# class Myclass:
#     def __init__(self):
#         self._protected_attr=20

# class Subclass(Myclass):
#     def __init__(self):
#         super().__init__()
#         print(self._protected_attr)

# obj1=Subclass()
# print(obj1._protected_attr)

# class Person:
#     def __init__(self):
#         self.__private_attr=1000

# class SubClass(Person):
#     def __init__(self):
#         super().__init__()
#         print(self.__private_attr)

# obj1=SubClass()

# class Myclass:
#     def __init__(self):
#         self.public_attr=100

#     def public_method(self):
#         return "This is public method"

# obj1=Myclass()
# print(obj1.public_attr)
# print(obj1.public_method())

# class Person:
#     def __init__(self):
#         self._protected_attr=1000

#     def _protected_method(self):
#         return "This is protected value"

# class Subclass(Person):
#     def __init__(self):
#         super().__init__()
#         print(self._protected_method())
#         print(self._protected_attr)

# obj1=Subclass()

# nums = [9,6,4,2,3,5,7,0,1]
# # Output: 8
# # Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
# list_len=len(nums)
# for i in range(0,len(nums)):
#     pass


# class Person:
#     __slots__ = ('name', 'age',)

#     def __init__(self,name,age,location):
#         self.name=name
#         self.age=age
#         self.location=location

# person1=Person("User1","23","indore")
# person2=Person("User2","34","Bhopal")

# print(person1.name)
# print(person1.age)
# print(person1.location)

# my_list=["apple","banana","cherry","pear"]
# for key,index in enumerate(my_list):
#     print(key,index)

# my_colors=["Red","Orange","green"]
# obj=enumerate(my_colors,100)
# for i in obj:
#     print(i)

# my_list1=[1,2,3,4,5,6]
# my_list2=["one","two","three","fourth","fifth"]

# zip_obj=zip(my_list1,my_list2)
# print(next(zip_obj))

# number=[1,2,3,4,5]
# letters=['a','b','c','d','e']

# zipped=zip(number,letters)
# print(zipped)
# print(next(zipped))

# zip_list=list(zipped)
# print(zip_list)

# import asyncio
# import time

# async def func1():
#     print("Function 1 is started")
#     await asyncio.sleep(10)
#     print("Function 1 is completed")

# async def func2():
#     print("Function 2 is started")
#     await asyncio.sleep(4)
#     print("Function 2 is completed")

# async def main():
#     start_time=time.time()
#     await asyncio.gather(func1(),func2())
#     end_time=time.time()
#     execuation_time=end_time-start_time
#     print(f"Time Taken for this{execuation_time}")

# if __name__=="__main__":
#     asyncio.run(main())
