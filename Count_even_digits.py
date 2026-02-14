num = int(input("enter a number: "))
#12345 - (2, 4) - count = 2
count = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        count += 1
    num //= 10
print("count of even digits:", count)