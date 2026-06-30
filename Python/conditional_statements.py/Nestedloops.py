"""
loop inside another loop
the inner loop completes all its iterations
for every single iteration of the outer loop
"""

#1 10 20 30 2 10 20 30 3 10 20 30

for i in range(1, 4):
    print(f"{i}", end= " ")
    for j in range(10, 31, 10):
        print(f"{j}", end= " ")

print()
#1 10 20 30 8 16 24 2 10 20 30 8 16 24 3 10 20 30 8 16 24

for i in range(1, 4):
    print(f"{i}", end= " ")
    for j in range(10, 31, 10):
        print(f"{j}", end= " ")
    for k in range(8, 25, 8):
        print(f"{k}",end = " ")