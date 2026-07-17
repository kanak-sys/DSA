"""
write a function power(base, exp)
that returns base
raised to exp
using a loop
no ** operator or pow is allowed
"""
def power(base, exp):
    
    i = 1
    start = 1
    while i<=exp:
        start = start * base
        i += 1
    return start

result = power(9, 4)
print(result)