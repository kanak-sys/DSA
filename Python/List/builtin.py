""" powerful builtins functions that operates directly on list """
marks = [10, 20, 30, 40, 50]
print(len(marks))  # length of list

print(max(marks))  # maximum value in list

print(min(marks))  # minimum value in list

print(sum(marks))  # sum of all numeric values in list

#it will always give u a new list
heyy = sorted(marks)
print(heyy)  # returns a new sorted list in ascending order

#for descending order, use reverse=True
heyy_desc = sorted(marks, reverse=True)
print(heyy_desc)  # returns a new sorted list in descending order