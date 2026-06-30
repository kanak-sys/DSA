"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""
for i in range(1, 6):
    for j in range(5, i-1, -1):
        print(f"{j}", end = " ")
    print()
"""
make it dynamic for suppose n = 7
7 6 5 4 3 2 1
7 6 5 4 3 2
7 6 5 4 3
7 6 5 4
7 6 5
7 6
7
""" 
n = int(input("enter the no. of lines: "))
for i in range(1, n+1):
    for j in range(n, i-1, -1):
        print(f"{j}", end = " ")
    print()