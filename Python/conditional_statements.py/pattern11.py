"""
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5

@ @ @ @ 1
@ @ @ 1 2
@ @ 1 2 3
@ 1 2 3 4
1 2 3 4 5

@ @ @ @ i = 1, k = 4
@ @ @   i = 2, k = 3
@ @     i = 3, k = 2
@       i = 2, k = 1


1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
for i in range(1, 6):
    for k in range(1, 6-i):
        print(f" ", end = " ")
    for j in range(1, i+1):
        print(f"{j}", end = " ")
    print()