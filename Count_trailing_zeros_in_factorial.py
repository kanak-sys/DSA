import math
n = int(input("enter a number :"))
fact = math.factorial(n)
# n= 5 fact = 120
fact_str = str(fact)
count = 0
for ch in reversed(fact_str):
    if ch == '0':
        count += 1
    else:
        break
#021 count = 1
print("Number of trailing zeros in", n, "factorial is:", count)