a = int(input("enter 1st number "))
b = int(input("enter 2nd number "))
#euclidean algorithm
while b != 0:
    a, b = b, a%b
print("GCD =",a)