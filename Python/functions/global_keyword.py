"""#without global keyword use
count = 0
def xyz():
    count = 1
    print(f"Inside function value: {count}")
xyz()
print(f"Outside function value: {count}")
"""

#with global keyword use
count = 0
def xyz():
    global count
    count = 2
    count += 3
    print(f"Inside function value: {count}")

xyz()
print(f"Outside function value: {count}")