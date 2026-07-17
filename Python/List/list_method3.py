"""methods for managing their overall state"""

#.copy()
"""return a new list by
creating a shallow copy of original
crucial when u want to modify a list without affecting its source"""

L1 = [10, 20, 30, 40]
L2 = L1.copy()
L2.append(50)
L2.insert(1,0)
print(L1)
print(L2)

#.clear()
"""Removes all items from the list.making it an empty list.
modifies the list in place"""

fruits = ['apple', 'banana', 'orange', 'mango', 'kiwi']
fruits.clear()
print(fruits)
