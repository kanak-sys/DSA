"""
ELEMENT wise sum of 2 lists:
given 2 list of same length,
write python code using a loop
to create a new list where
each elements is the sum of the corresponding elements
of the 2 lists

l1=[10, 20, 30, 40]
l2=[1, 2, 3, 4]
output: [11, 22, 33, 44]

"""
list1 = [23, 76, 45, 19, 8, 65, 76]
list2 = [-2, 8, -1, 0, 19, 65, 51]
def elementwise_sum(list1, list2):
    new_list = []
    n = len(list1)
    for i in range(n):
        total = list1[i] + list2[i]
        new_list.append(total)
    return new_list

answer = elementwise_sum(list1, list2)
print(answer)