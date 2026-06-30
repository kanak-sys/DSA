"""
Ask a number from the user
and print all the factors

enter a no. - 10
factors: 1 2 5 10
"""
num = int(input("enter no. - "))
i = 1
while i <= num:
    if num % i == 0:
        print(f"factors of {num} - {i}")
    i += 1

"""
count all the factors and return total
"""
num1 = int(input("enter no.  - "))
j = 1
count = 0
while j <= num1:
    if num1 % j == 0:
        count += 1
    j += 1
print(f"total factors of {num1}: {count}")