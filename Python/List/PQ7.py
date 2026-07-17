"""Reverse the list without using .reverse() method or list slicing[::-1]
think about swapping elements from both ends of a list using a loop
"""

def reverse_list(list):
    n = len(list)
    new_list = []
    for i in range(n-1, -1, -1):
        new_list.append(list[i])
    return new_list

list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverse_list(list))