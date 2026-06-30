"""
write a function called add
that takes 2 numbers as parameters
and prints their sum

"""
def add(num1, num2):
    sum = num1 + num2
    print(f" The sum of 2 entered number: {sum} ")
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
add(n1, n2)