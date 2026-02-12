n = int(input("enter a number:"))
n = abs(n)
smallest = 9
while n > 0:
    digit = n%10
    if digit < smallest:
        smallest = digit
    n //= 10
print("smallest digit is: ", smallest)