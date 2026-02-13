#divide the no by 2
#note remainde(0 or 1)
#divide again by 2
#repeat until the no becomes 0
#reverse the remainders
n = int(input("Enter a decimal number: "))
p = n
binary = ""
while n > 0:
    binary = str(n%2) + binary
    n //= 2
print("Binary of decimal no ",p,"is",binary)