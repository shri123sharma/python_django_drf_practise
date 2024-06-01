# def decorator_func(func):
#     def wrapper():
#         print("before excuation this decorator func")
#         result=func()
#         print(result)
#         print("after excuation this decortor func")
#     return wrapper

# @decorator_func
# def say_hello():
#     return "Hello_World"
# say_hello()

# ls1=[1,2,3,4,5,6,7,8,9,10]
# t1=(10,20,30,40,50,60,70,80)
# s1={100,200,300,400,500}
# d1={'value1':1000,'value2':2000,'value3':3000,'value4':40000}

# for i in ls1:
#     print(i)
# print(dir(ls1))
# print(ls1.__add__)
# print(ls1.__class__)

# def gen_func():
#     sum=0
#     for i in range(0,10):
#         sum+=i
#         yield sum

# if __name__=="__main__":
#     result=gen_func()
#     print(next(result))
#     print(next(result))
#     print(next(result))

# lst1=[10,20,30,40,50,60]
# lst2=lst1.copy()
# print(lst2)
# lst2[0]=100
# print(lst2)

# ls1=[10,20,[1,2,3,4],40,50]
# ls2=ls1.copy()
# print(ls1)
# print(ls2)
# ls2[2][1]="10000"
# print(ls2)
# print(ls1)

# import copy
# ls1=[1,2,3,4,[100,200,300,400]]
# ls2=copy.deepcopy(ls1)
# ls2[4][0]="AAAAAA"
# print(ls2)
# print(ls1)

# import threading
# import time

# def task1():
#     for i in range(5):
#         print(i)
#         time.sleep(1)

# def task2():
#     for j in "ABCDE":
#         print(j)
#         time.sleep(1)

# thread1=threading.Thread(target=task1)
# thread2=threading.Thread(target=task2)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# import multiprocessing
# import multiprocessing.pool
# import time

# def task1(n):
#     return n*n

# def task2(n):
#     return n+n

# if __name__=="__main__":
#     number=[1,2,3]
#     with multiprocessing.Pool() as pool:
#         start_time=time.time()
#         result_square=list(map(task1,number))
#         result_add=list(map(task2,number))
#         end_time=time.time()
#         print(f"Total time excuation for{end_time-start_time}")
#         print(result_square)
#         print(result_add)


# def outer_func(x):
#     def inner_func(y):
#         return x+y
#     return inner_func

# if __name__=="__main__":
#     closure=outer_func(10)
#     print(closure(1))

# is_even=lambda x:x%2==0
# for i in range(1,10):
#     print(is_even(i))

# def func(n):
#     if n%2==0:
#         print("Even")
#     else:
#         print("Odd")

# if __name__=="__main__":
#     number=[1,2,3,4,5]
#     result=list(map(func,number))
#     print(next(result))


# def func(n):
#     if n%2==0:
#         return n

# if __name__=="__main__":
#     number=[1,2,3,4,5,6]
#     result=list(filter(func,number))
#     print(result)

# class Myclass:
#     class_var=100
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def instance_method(self):
#         return self.name+self.age+str(self.class_var)

# obj1=Myclass("user1","23")
# print(obj1.instance_method())

# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area():
#         pass

#     @abstractmethod
#     def parameter():
#         pass

# class Circle(Shape):
#     a=10
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return self.radius*3.14*self.a

#     def parameter(self):
#         return 2*3.14*self.radius

# obj1=Circle(100)
# print(obj1.area())
# print(obj1.parameter())

# class Mymetaclass(type):
#     def __new__(cls,name,bases,dct):
#         print("Creating class",name)
#         dct['custom_attribute']="this is custom attribute"
#         return super().__new__(cls,name,bases,dct)

# class Myclass(metaclass=Mymetaclass):
#     pass

# print(Myclass.custom_attribute)

# class Myclass:
#     def __new__(cls):
#         print("New instance is created")
#         return super().__new__(cls)

#     def __init__(self,value):
#         print("Intializing new instance")
#         self.value=value
#         return self.value

# obj1=Myclass
# print(obj1.__new__)


# class Myclass:
#     class_variable=100
#     def __init__(self):
#         self.name="Shri"
#         self.age=24

#     def instance_method(self):
#         return f"instance attribute is get:-{self.name} and {self.age} and {self.class_variable}"

# obj1=Myclass()
# print(obj1.instance_method())

# class MyClass:
#     class_variable="This is class Variable"
#     def __init__(self,company,location):
#         self.company=company
#         self.location=location

#     @classmethod
#     def myclassmethod(cls):
#         return cls.class_variable
# obj1=MyClass("TCS","Indore")
# print(obj1.myclassmethod())

# class MyStaticClass:
#     @staticmethod
#     def sum_value():
#         sum=0
#         for i in range(10):
#             sum+=i
#         return sum

# obj1=MyStaticClass()
# print(obj1.sum_value())


# class PublicClass:
#     def __init__(self,name):
#         self.name=name

#     def public_method(self):
#         return "This is public method"

# obj1=PublicClass("User_test")
# print(obj1.name)
# print(obj1.public_method())

# class ProtectClass:
#     def __init__(self,employee,workplace):
#         self._employee=employee
#         self._workplace=workplace

#     def _protect_method(self):
#         return "this is protect attribute"

# obj1=ProtectClass("Emplyee-1","TCS")
# print(obj1._employee)
# print(obj1._protect_method())


# class PrivateClass:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age

#     def __privatemethod(self):
#         return self.__name+self.__age

# obj1=PrivateClass("user1",23)
# print(obj1.__privatemethod())

# class SlotClass:
#     __slot__=("name","age",)

#     def __init__(self,name,age,location):
#         self.name=name
#         self.age=age
#         self.location=location

#     def slotmethod(self):
#         return f"this is slot method to used for memory efficient:-{self.name}-{self.age}-{self.location}"

# obj1=SlotClass("test-user",23,"indore")
# print(obj1.slotmethod())

# import time
# def task1():
#     print("task1 is started")
#     time.sleep(3)
#     print("task1 is completed")

# def task2():
#     print("task2 is started")
#     time.sleep(4)
#     print("task2 is complted")

# if __name__=="__main__":
#     start_time=time.time()
#     task1()
#     task2()
#     end_time=time.time()
#     total_time=end_time-start_time
#     print(f"Total time to completed two task {total_time}")


# import asyncio
# import time

# async def task1():
#     print("task1 is started")
#     await asyncio.sleep(3)
#     print("task1 is completed")

# async def task2():
#     print("task2 is started")
#     await asyncio.sleep(10)
#     print("task2 is completed")

# async def main():
#     start_time=time.time()
#     await asyncio.gather(task1(),task2())
#     end_time=time.time()
#     execute_time=end_time-start_time
#     print(f"Total excuated time:-{execute_time}")

# if __name__=="__main__":
#     asyncio.run(main())

# class Myobject:
#     def __init__(self,number):
#         self.num=number

#     def sort(self):
#         for i in range(0,len(self.num)):
#             for k in range(i+1,len(self.num)):
#                 if self.num[i]>=self.num[k]:
#                     self.num[i],self.num[k]=self.num[k],self.num[i]
#         return self.num
# number=[3,5,7,8,3,6,3,7,1]
# obj1=Myobject(number)
# print(obj1.sort())

# import numpy as np
# arr1d=np.array([1,2,3,4,5,6])
# print(type(arr1d))
# print(arr1d)

# arr2d=np.array([[1,2,3],
#                [4,5,6],
#                [7,8,9]])
# print(arr2d)

# class MyOverloadingClass:
#     def show_data(self,*args):
#         sum=0
#         for i in args:
#             sum+=i
#         return sum

# obj1=MyOverloadingClass()
# print(obj1.show_data(10,20,40,37,43,45))

# ls1=[1,2,3,3,7,4,4,9]
# l1=[]
# l2=[]
# for i in ls1:
#     if i not in l1:
#         l1.append(i)
#     else:
#         l2.append(i)
# print(l1)
# print(l2)

# import time
# import threading

# def task1():
#     for i in range(1,5):
#         print(f"Numbers:-{i}")
#         time.sleep(1)

# def task2():
#     for k in "ABCDE":
#         print(f"letters:-{k}")
#         time.sleep(4)

# if __name__=="__main__":
#     t1=threading.Thread(target=task1)
#     t2=threading.Thread(target=task2)

#     t1.start()
#     t2.start()

#     star_time=time.time()
#     t1.join()
#     t2.join()
#     end_time=time.time()
#     print(f"this is total execuation time {end_time-star_time}")

# import multiprocessing
# import time

# def print_numbers():
#     for i in range(5):
#         print(f"Number: {i}")
#         time.sleep(1)

# def print_letters():
#     for letter in 'abcde':
#         print(f"Letter: {letter}")
#         time.sleep(1)

# if __name__ == '__main__':
#     # Creating processes
#     p1 = multiprocessing.Process(target=print_numbers)
#     p2 = multiprocessing.Process(target=print_letters)

#     # Starting processes
#     p1.start()
#     p2.start()

#     # Waiting for processes to complete
#     p1.join()
#     p2.join()

#     print("Done!")

# import multiprocessing
# import time

# def task1():
#     for i in range(5):
#         print(f"this is number:-{i}")
#         time.sleep(1)

# def task2():
#     for k in "ABCDE":
#         print(f"this is letters:-{k}")
#         time.sleep(3)

# if __name__=="__main__":

#     p1=multiprocessing.Process(target=task1)
#     p2=multiprocessing.Process(target=task2)

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print("Done!")


# input_var="aabcddeff"
# # op="a2b1c1d2e1f2"
# count=1
# str_val=""
# for i in range(0,len(input_var)):
#     for j in range(i+1,len(input_var)):
#         if input_var[i]==input_var[j]:
#             count+=1

#         else:
#             pass
# print(count)

# input_var ="aabcddeff"
# str_op=""

# count=1
# for i in range(len(input_var)):
#     if i<len(input_var)-1 and  input_var[i] ==input_var[i+1]:
#         count+=1
#     else:
#         str_op+=input_var[i]+str(count)
#         count=1

# print(str_op)

# ls1=[1,2,3,4,5,6,5,3,5]
# unique_ls1=[]
# duplicate_list=[]
# for i in ls1:
#     if i not in unique_ls1:
#         unique_ls1.append(i)
#     else:
#         duplicate_list.append(i)

# print(unique_ls1)
# print(duplicate_list)
