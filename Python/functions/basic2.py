"""
write a function that prints
all the factors of a number 
enteredd by user
"""
def factors():
    num = int(input("enter a number: "))
    i = 1
    while i <= num:
        if num % i == 0:
            print(f"{i}", end=" ")
        i += 1
factors()