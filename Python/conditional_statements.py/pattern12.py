"""
        5
      5 4
    5 4 3
  5 4 3 2
5 4 3 2 1

@ @ @ @ 5
@ @ @ 5 4
@ @ 5 4 3
@ 5 4 3 2
5 4 3 2 1

@ @ @ @  i=5 k=4 
@ @ @    i=4 k=3
@ @      i=3 k=2
@        i=2 k=1
         i=1 k=0

5
5 4 
5 4 3
5 4 3 2
5 4 3 2 1
"""
for i in range(5, 0, -1):
    for k in range(1, i):
        print(f" ", end=" ")
    for j in range(5, i-1, -1):
        print(f"{j}", end = " ")
    print()