"""
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1

@ @ @ @ 1          i=1
@ @ @ 1 2 3        i=2
@ @ 1 2 3 4 5      i=3
@ 1 2 3 4 5 6 7    i=4
1 2 3 4 5 6 7 8 9  i=5

1                  i=1 j=1*2-1
1 2 3              i=2 j=2*2-1
1 2 3 4 5          i=3 j=3*2-1
1 2 3 4 5 6 7      i=4 j=4*2-1
1 2 3 4 5 6 7 8 9  i=5 j=5*2-1

@ @ @ @  i=1 k=4(6-1)
@ @ @    i=2 k=3(6-2)
@ @      i=3 k=2(6-3)
@        i=4 k=1(6-4)
         i=5 k=0(6-5)


@ 1 2 3 4 5 6 7  i=4
@ @ 1 2 3 4 5    i=3
@ @ @ 1 2 3      i=2
@ @ @ @ 1        i=1

try
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

"""
for i in range(1, 6):
    for k in range(1, 6-i):
        print(f" ",end = " ")  #f"@"
    for j in range(1, (i*2)-1+1):
        print(f"{j}", end = " ")
    print()
for i in range(4, 0, -1):
    for k in range(1, 6-i):
        print(f" ",end = " ")   #f"@"
    for j in range(1, (i*2)-1+1):
        print(f"{j}", end = " ")
    print()


for m in range(1, 6):
    for n in range(1, 6-m):
        print(f" ",end = " ")  #f"@"
    for o in range(1, (m*2)-1+1):
        print(f"*", end = " ")
    print()
for m in range(4, 0, -1):
    for n in range(1, 6-m):
        print(f" ",end = " ")   #f"@"
    for o in range(1, (m*2)-1+1):
        print(f"*", end = " ")
    print()
