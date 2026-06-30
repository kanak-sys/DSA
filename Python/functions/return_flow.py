"""
return true if a number is prime
17 -1, 17
3 -1, 3
19 -1, 19
"""

def is_prime(number):
    count = 0
    i = 1
    for i in range(1, int(number/2) + 1):
        if number % i == 0:
            count += 1
        i += 1

    if count > 2:
        return False
    else:
        return True
        
n1 = int(input("Enter number: "))
ans = is_prime(n1)
print(f"prime? {ans}")


def greet(name, age):
    return f"your name is: {name}, and age is: {age}"
print(greet("kanak", 20))