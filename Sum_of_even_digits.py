num = int(input("enter a number:"))
sum = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        sum += digit
    num //= 10
print("sum of even digits:", sum)