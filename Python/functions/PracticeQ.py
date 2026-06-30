"""
write a function fizzbuzz(n)
that takes single number and prints
fizz if it is divisible by 3
buzz if it is divisible by 5
fizzbuzz if it is divisible by both
otherwise print the number itself
"""
def fizzbuzz(num1):
    if num1 % 3 == 0 and num1 % 5 == 0:
        print(f"FizzBuzz")
    elif num1 % 3 == 0:
        print(f"Fizz")
    elif num1 % 5 == 0:
        print(f"Buzz")
    else:
        print(f"{num1}")
fizzbuzz(15)
fizzbuzz(81)
fizzbuzz(25)
fizzbuzz(17)