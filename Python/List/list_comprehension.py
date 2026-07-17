"""
creates a new list
basic usage:For loop v/s one line
transforming a loop that builds a list into a single comprehension
"""
#normal way
squares = []
for i in range(1, 6):
    squares.append(i * i)
print(squares)

#comprehension
squares1 = [i * i for i in range(1, 6)]
print(squares1)

#normal way
evenn = []
for i in range(1, 21):
    if i % 2 == 0:
        evenn.append(i)
print(evenn)

#comprehension
evenn1 = [i for i in range(1, 21) if i % 2 == 0]
print(evenn1)

"""
transforming elements:
"""

names = ['rahul', 'rina', 'riya', 'ritu']
upper = [name.upper() for name in names]
print(upper)