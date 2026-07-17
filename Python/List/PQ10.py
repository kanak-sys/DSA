"""separate a list of integers into two distinct list
one containing all the even numbers
and the other containing all the odd numbers"""

def separate_int(list):
    l1 = []
    l2 = []
    for num in list:
        if num % 2 == 0:
            l1.append(num)
        else:
            l2.append(num)
    print(f"Even list", {l1})
    print(f"odd list", {l2})
list = [2, 4, 3, 5, 2, 1, 0, 7, 5, 6, 8]
print(separate_int(list))
