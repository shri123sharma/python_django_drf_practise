# def func(a:int,b:int):
#     return a+b
# result=func(10,20)
# print(result)

def func1(a:int,b:int):
    return a+b
result=func1(10,20)
print(result)

def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator
for i in countdown(5):
    print(i)

