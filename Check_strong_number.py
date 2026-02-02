num = int(input("enter a number "))
temp = num
sumf = 0
def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
while temp > 0:
    digit = temp % 10
    sumf += fact(digit)
    temp //= 10
if sumf == num:
    print("strong number")
else:
    print("not a strong number")