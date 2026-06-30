"""
ask a no. from user and print multiplication table upto 10
"""
num = int(input("enter a no.: "))
i = 1
while (i <= 10):
    print (f"{num} * {i} = {num * i}")
    i += 1
