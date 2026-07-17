"""Given 2 list merge them into a single new list,without modifying the originals
use the + operator or a loop to combine
"""
def merge_list(list1, list2):
    new_list = []
    for num in list1:
        new_list.append(num)
    for nums in list2:
        new_list.append(nums)
    return new_list

def merge_lst(lst1, lst2):
    return lst1 + lst2

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(merge_lst(list1, list2))
print(merge_list(list1, list2))