a = int(input("enter 1st number "))
b = int(input("enter 2nd number"))
x, y = a, b
while y != 0:
    x, y = y, x%y
gcd = x
lcm = (a*b)//gcd
print("LCM = ", lcm)