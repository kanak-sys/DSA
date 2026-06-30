"""
write a function that ask a number from user
and prints if that no. is odd or even
"""
def odd_even():
    num = int(input("enter a number: "))
    if num % 2 == 0:
        print(f"even: {num}")
    else:
        print(f"odd: {num}")
odd_even()