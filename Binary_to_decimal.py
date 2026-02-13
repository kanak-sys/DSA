#bit - 101100 after reversing
#postion/power - 0 1 2 3 4 5
#2^0=1 2^1=2 2^2=4 2^3=8 2^4=16 2^5=32 .. 1 2 4 8 16 32
#1 * 1= 1 
#0 * 2= 0
#1 * 4= 4 ...
# 1 * 32= 32
# 1 + 0 + 4 + 0 + 0 + 32 = 37
n = input("Enter a binary number: ")
decimal = 0
power = 0
for digit in reversed(n):  # if n = 110 then reversed(n) = 011
    decimal += int(digit) * (2 ** power)
    power += 1
print("Decimal of binary no ",n,"is",decimal)
