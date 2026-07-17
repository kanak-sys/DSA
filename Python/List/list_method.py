"""
Built-in List functions in Python
that operate directly on list
methods change the original list and return None
"""
#Append:
"""
Adds a single element to the end of the list

"""
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)  

#Insert:
"""
Insert an element at a specified index
first argument = index,
second argument = element to insert
"""
fruitss = ['apple', 'banana', 'cherry']
fruitss.insert(1, 'orange')
print(fruitss)

#Remove: by value
"""
Removes the first occurrence of a specified element
if the element is not found, it raises a ValueError
"""
fruitsss = ['apple', 'banana', 'cherry']
fruitsss.remove('banana')
print(fruitsss)

#Pop: remove by index
"""
removes and returns the element at the specified index
if no index is specified, it removes the last item and returns it
"""
fruitssss = ['apple', 'banana', 'cherry']
fruitssss.pop()
print(fruitssss, id(fruitssss))  #id() function returns the identity of an object. 

fruitssss.pop(1)
print(fruitssss, id(fruitssss)) #id() same after changes which means the original list 
                                    #is modified

fruitsssss = ['kiwi','apple', 'banana', 'cherry']
popped_fruit = fruitsssss.pop(0)
print(popped_fruit)
print(fruitsssss)