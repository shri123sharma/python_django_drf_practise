def func(a:int,b:int):
    return a+b
result=func(10,20)
print(result)

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