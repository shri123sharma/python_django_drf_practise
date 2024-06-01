# 1.immediateSmaller
def immediateSmaller(arr, n):
    ls1 = []
    if arr[-1] == -1:

        return ls1.append(-1)
    else:
        for i in range(n+1):
            for j in range(i+1, n):
                if arr[i] > arr[j]:
                    ls1.append(arr[j])
                else:
                    ls1.append(-1)
            return ls1


if __name__ == "__main__":
    number_arr = [4, 2, 1, 5, 3]
    # number_arr=[5, 6, 2, 3, 1, 7]
    num_length = len(number_arr)
    result = immediateSmaller(number_arr, num_length)
    print(result)

# 2.immediateSmaller


class Solution:
    def immediateSmaller(self, arr, n):
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i] = arr[i+1]

            else:
                arr[i] = -1

        arr[n-1] = -1
        return arr


if __name__ == "__main__":
    num_list = [4, 2, 1, 5, 3]
    num_len = len(num_list)
    obj1 = Solution()
    result = obj1.immediateSmaller(num_list, num_len)
    print(result)

# Subset Two array
ls1 = [1, 4, 6, 8, 3, 26, 8]
max_val = 0
for i in range(0, len(ls1)):
    for k in range(i+1, len(ls1)):
        if ls1[i] <= ls1[k]:
            max_val = ls1[k]
        else:
            max_val
print(max_val)

ls1 = [1, 4, 2, 5, 2, 6, 8, 9, 4, 11]
max_val = ls1[0]
for i in ls1:
    if i > max_val:
        max_val = i
print(max_val)


def maximum_and_minimum(array):
    if not array:
        return None, None
    max_num = min_num = array[0]
    for num in array:
        if num >= max_num:
            max_num = num
        elif num <= min_num:
            min_num = num
    return max_num, min_num


if __name__ == "__main__":
    ls1 = [1, 2, 3, 1, 0, 6, 3, 14]
    result = maximum_and_minimum(ls1)
    print(result)


def reverse_string(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str


# Example usage:
my_string = "Hello, world!"
reversed_string = reverse_string(my_string)
print(reversed_string)


def prime_number(Num):
    pass


if __name__ == "__main__":
    num = int(input("Enter a number if Check its prime or not"))
    result = prime_number(num)
    print(result)
