num = int(input("enter a number:"))
sum_d = 0
while num > 0:
    digit = num % 10
    sum_d = sum_d + digit
    num = num // 10
print("the sum of digits:", sum_d)