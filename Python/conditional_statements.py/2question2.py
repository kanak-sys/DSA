"""
take 2 numbers as input
print the greater of two
if they are equal print both numbers are equal"""

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
if num1 == num2:
    print(f"both numbers are equal: {num1}")
elif num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")