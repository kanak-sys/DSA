"""
small anonymous function written in single line
useful when u need a simple function for a short period
do not want to formally define it with def
"""

#normal function
#def square(n):
#   return n * n

#same thing as a lambda
square = lambda n: n * n

print(square(8))

#def can_vote(age):
#    if age >= 18:
#        return True
#    return False

can_vote = lambda age: True if age>= 18 else False
print(can_vote(4))