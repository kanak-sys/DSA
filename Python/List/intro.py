#datatype
"""
so far, a variable stores 1 value at a time
but what if you need to store
the marks of 5 studs or names of 10 cities

using list
a collection that stores multiple values in a single variable;;

properties:
ordered- items stay in exact order u put in.
mutable- u can change, add or remove items anytime
allows duplicacy- same value can appear more than once
any type of data- can hold integer, boolean, string, or even other lists
"""

#without list
stud1 = "kanak"
stud2 = "abhishek"
stud3 = "tisha"

#with list
studs = [1, 2, 3, 4, 5]
print(type(studs))

#list operation behaviour - +,-,/,*
print(studs + [6, 7, 8])  # concatenation
print(studs - [1, 2])  # not supported
print(studs * 4)  # repetition
print(studs * [1, 2])  # not supported
print(studs / 2)  # not supported
print(studs // 2)  # not supported
