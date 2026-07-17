"""
check if the list is sorted:
wap that takes a list of numbers,
and using a loop,
determines whether it is
sorted in ascending order
print true if it is sorted, else print false
do not use built in sorted() function

numbers = [10, 7, 34, 20, 4, 45, 86, 2, 90, 51, 1, 99]
expected output: False

"""


def is_sorted(list):
    n = len(list)
    i = 0
    for i in range(0, n-1):
        if list[i] > list[i + 1]:
            return False
        i += 1
    return True
list = [3, 5, 7, 9, 11, 13, 15, 17, 19]

print(is_sorted(list))
