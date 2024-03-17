
import cProfile


def greet(num):
    for i in range(num):
        if i % 2 == 0:
            print("True")
        else:
            print("False")


def add_number(a: list, b: list):
    print(a.extend(b))


my_variable = "This is a variable from my_module"


class MyClass:
    def __init__(self):
        self.__private_value = 100

    def get_private_value(self):
        return self.__private_value


obj1 = MyClass()
print(obj1.get_private_value())


class MyClass1:
    def __init__(self):
        self.__private_attribute = 100

    def get_private_attribute(self):
        return self.__private_attribute

    def set_private_attribute(self, value):
        self.__private_attribute = value


obj = MyClass1()
print(obj.get_private_attribute())
obj.set_private_attribute(19999)
print(obj.get_private_attribute())


def myfunc():
    lst = []
    for i in range(10):
        val = i**i
        lst.append(val)
    return lst


if __name__ == "__main__":
    cProfile.run("myfunc()")


def func(num, ls1):
    ls2 = []
    ls3 = []
    for i in range(0, num):
        if i not in ls2:
            ls2.append(ls1[i])
        else:
            ls3.append(i)
    return str(ls3)


N = 4
ls1 = [0, 3, 1, 2]
print(func(N, ls1))


def func_result(seen, duplicate):
    if duplicate:
        return list(duplicate)

    else:
        return [-1]


def find_duplicate(arr):
    seen = set()
    duplicate = set()
    for i in arr:
        if i in seen:
            duplicate.add(i)

        else:
            seen.add(i)

    result = func_result(seen, duplicate)
    return result


N = 5
# ls1=[0,3,1,2]
ls1 = [2, 3, 1, 2, 3]
print(find_duplicate(ls1))

ls1 = [1, 2, 3, 4, 16, 5, 22, 6, 6, 7, 7]
ls1.sort()
print(ls1)

ls2 = [1, 6, 9, 4, 2, 6, 8, 7, 3, 100]
ls3 = sorted(ls2)
print(ls2)
print(ls3)


pdb.set_trace()
