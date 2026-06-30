"""
write a function called find_max,
that takes 3 numbers as parameters
and prints the largest one

"""
def find_max(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f"the maximum number: {num1}")
    elif num2 > num3 :
        print(f"the maximum number: {num2}")
    else:
        print(f"the maximum number: {num3}")
n1 = int(input("enter number1 : "))
n2 = int(input("enter number2 : "))
n3 = int(input("enter number3 : "))
find_max(n1, n2, n3)