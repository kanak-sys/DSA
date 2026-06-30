"""
print all the numbers which are divisible by
3 and 5 between 1 to 100
"""
start = 1
end = 100
i = start
while i <= end:
    if (i % 3 == 0) and (i % 5 == 0):
        print(f"the no divisible by 3 and 5 in between 1 to 100 is: {i}")
    i += 1
print("done")