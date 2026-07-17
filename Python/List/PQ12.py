"""Given a list of numbers (which may contain duplicates),
write a python script that takes an integer as input
from the user and removes all occurence of that integer
from the list"""

list = [1, 3, 45, 83, 1, 47, 7, 23, 6, 87, 34, 1, 6, 67, 47, 98, 1, 23, 65, 83]
num = int(input("Enter no. whose occurence u would like to remove: "))

def remove_occurence(list, num):
    new_l1 = []
    for n in list:
        if n != num:
            new_l1.append(n)

    return new_l1
print(remove_occurence(list, num))