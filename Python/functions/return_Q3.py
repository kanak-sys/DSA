"""
write a function called absolute_value
that takes a number
and returns its absolute value
without using the built-in abs() function
"""
def absolute_value(n1):
    if n1 >= 0:
        return n1
    else:
        return n1 * -1
result = absolute_value(-10)
print(result)