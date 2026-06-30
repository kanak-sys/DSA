"""
Basic in for loop

print 1 to 10 using for loop
"""
for i in range(1,11):
    print(f"{i}")

"""
steps in for loop: by default 1 
1 3 5 7 9
"""

for i in range(1,11,2):
    print(f"{i}")

# -5 -1 3 - steps

for i in range(-5, 5, 4):
    print(f"{i}")

"""
negative for loop:
10 to 1
-1 steps
"""

for i in range(10, 0, -1):
    print(f"{i}")