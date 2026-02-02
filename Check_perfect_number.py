num = int(input("enter a number "))
sumD = 0
for i in range(1, num):
    if num % i == 0:
        sumD += i

if sumD == num:
    print("perfect number")
else:
    print("not a perfect number")