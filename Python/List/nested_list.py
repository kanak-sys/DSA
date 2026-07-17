"""
essentially a list that contain other list as its elements
allows us to represent complex data such as grids, tables, matrix"""

#3*3 matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
        ]

"""use multiple indexer for accessing"""
print(matrix)
print(matrix[0])        #[1, 2, 3]
print(matrix[1])        #[4, 5, 6]
print(matrix[1][2])     #6
print(matrix[2][0])     #7

"using for loop accessing all elements"

for i in range(0, 3):
    for j in range(0, 3):
        print(matrix[i][j], end = " ")
    print()

"print total of all elements"

total = 0
for i in range(0, 3):
    for j in range(0, 3):
        total += matrix[i][j]
print(f"total of all elements in nested list: {total}")

"dyanamic accessing of element 4*6(let)"

mat = [[1,2,3,4,5,6],
       [4,5,6,7,8,9],
       [1,3,5,7,9,1],
       [1,4,7,0,3,6]]

rows = len(mat)
columns = len(mat[0])
print(rows)
print(columns)
for i in range(0, rows):
    for j in range(0, columns):
        print(mat[i][j],end = " ")
    print()