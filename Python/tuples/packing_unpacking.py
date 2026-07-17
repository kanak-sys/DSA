hey = 1, 2, 3, 4
print(hey)
print(type(hey))
tuple = 1,
print(tuple)
print(type(tuple))
inth = 1
print(inth)
print(type(inth))

#unpacking
a, b, c, d = 1, "surat", True, 4
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

#a, b, c = 1, "surat", True, 4 # error needed 3 got 4

#make a function that returns min and max of a list

def min_maxi(list):
    mini = min(list)
    maxi = max(list)
    return mini, maxi #retuns tuple as it does unpacking
list = [9, 87, 45, 23, 96, 78, 0, -2]
ans1, ans2 = min_maxi(list)
print(f"maximum = {ans2}, minimum = {ans1}")