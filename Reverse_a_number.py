def revNum(n):
    rev = 0
    while n > 0 :
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
n = int(input("enter a number: "))
print("The reverse of the number is:", revNum(n))