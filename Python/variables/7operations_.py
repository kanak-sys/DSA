"""
order(Highest to Lowest) of operations
** -> exponentiation
* / // % -> multiplication, division, floor division, modulus
+ - -> addition, subtraction
"""
#don't forget to use parenthesis to change the order of operations
print(2 + 3 * 4) #14, not 20
print((2 + 3) * 4) #20, not 14

print(10 - 2 ** 3 ) # 2, not 512
print((10 // 2 + 3)) # 8, not 2.5

print((10 - 2) ** 3) #512, not 2

"""
Comparison Operators compares and always returns boolean value True or False
=(equal to),
!=(not equal to),
>(greater than),
<(less than),
>=(greater than or equal to),
<=(less than or equal to)
"""

a = 10
b = 20
print(a == b) #False
print(a != b) #True
print(a > b) #False
print(a < b) #True
print(a >= b) #False
print(a <= b) #True

"""
Logical Operators are used to combine conditional statements returns boolean value
and,
or,
not"""

#And, Or, Not
Chemistry = 45
Physics = 55
print(Chemistry > 50 and Physics > 50) #False
print(Chemistry > 50 or Physics > 50) #True

print(not(Chemistry > 50) and not(Physics > 50)) #True
