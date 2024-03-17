from abc import ABC, abstractmethod


def StringChallenge(s):
    words_to_digits = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # Replace written-out numbers with digits
    for word, digit in words_to_digits.items():
        s = s.replace(word, digit)

    # Replace "minus" with "-"
    s = s.replace('minus', '-')

    # Replace "plus" with "+"
    s = s.replace('plus', '+')

    # Manually evaluate the expression
    try:
        result = eval(s)
    except:
        return "Invalid expression"

    # Check if the result is negative
    if result < 0:

        result_in_words = 'neg' + '-'.join(['-' + char + '-' for char in 'ative']) + ''.join(
            words_to_digits[digit] for digit in str(-result))
    else:
        result_in_words = ''.join(
            words_to_digits[digit] for digit in str(result))

    return result_in_words


# Test cases
print(StringChallenge("oneminusoneone"))  # Output: neg--a--tiveonezero
print(StringChallenge("onezeropluseight"))  # Output: oneeight


class FileManger:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f"File '{self.filename}' opened in '{self.mode}' mode.")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print(f"File '{self.filename}' closed.")

        if exc_type is not None:
            print(
                f"An exception of type {exc_type} occurred with message: {exc_value}")

        return False


file_name = "context.txt"
with FileManger(file_name, "w") as file:
    file.write("hello i am python developer")


class MetaClass(type):
    def __new__(cls, name, bases, dct):
        dct['custom_attribute'] = 40
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MetaClass):
    pass


obj = MyClass()
print(obj.custom_attribute)


class Drawable(ABC):
    @abstractmethod
    def area(self):
        return "hello this is abstract method"


class Circle(Drawable):
    # def area(self):
    #     return "hello world"
    pass


obj1 = Circle()
print(obj1.area())
