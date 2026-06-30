"""
write a function called min_of_three
that takes three number
and returns the smallest
without using any built in function

"""
def min_of_three(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n3:
        return n2
    else:
        return n3
result = min_of_three(13, 6, 31)
print(result)