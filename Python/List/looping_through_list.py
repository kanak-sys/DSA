"""

fundamental operation

"""
#using a for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# using range and len in for loop
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])

# using a for loop to iterate in reverse order
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)-1, -1, -1):
    print(fruits[i])

# using a for loop to iterate in reverse order
fruits = ["apple", "banana", "cherry"]
for fruit in fruits[::-1]:
    print(fruit)

#using a while loop
fruits = ["apple", "banana", "cherry"]
i = 0
while i < (len(fruits)-1):
    print(fruits[i])
    i += 1

# using a while loop to iterate in reverse order
fruits = ["apple", "banana", "cherry"]
n = len(fruits)
j = n-1
while j >= 0:
    print(fruits[j])
    j -= 1