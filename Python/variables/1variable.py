"""variable must start with a letter or _
can't be a keyword and can't contain spaces/hypens- and can't start with a number
names are case sensitive  i.e. ab != AB or Ab """

name, age, gender = 'rahul', 25, "male"
is_student = True
print(age)
print(gender)
print(name, age, gender)

""" every value in python has a type, 
data types
1. int
2. float
3. str
4. bool

"""
print(type(name))
print(type(age))
print(type(gender))
print(type(is_student))