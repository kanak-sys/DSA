"take a nested list from user and"
"check if the given matrix is a sqaure matrix, "
"print its upper triangle as it is "
"replace its lower triangle with '*' "

"""
1 2 3
* 4 5
* * 6

"""
import ast
list = input("enter a nested list e.g[[1,2],[1,2]]: ")
nested_list = ast.literal_eval(list)
print("entered data: {nested_list1}")

rows = len(nested_list)
columns = len(nested_list[0])

if rows == columns:
    for i in range(0, rows):
        for j in range(0, columns):
            if i <= j:
                print(nested_list[i][j], end = " ")
            else:
                print("*", end = " ")
        print()

"""
1 * *
* 2 *
* * 3
"""

import ast
list1 = input("enter a nested list e.g[[1,2],[1,2]]: ")
nested_list1 = ast.literal_eval(list)
print("entered data: {nested_list1}")

rows1 = len(nested_list1)
columns1 = len(nested_list1[0])

if rows1 == columns1:
    for m in range(0, rows1):
        for n in range(0, columns1):
            if m == n:
                print(nested_list1[m][n], end = " ")
            else:
                print("*", end = " ")
        print()

"""
* * 1
* 2 *
3 * *
"""
import ast
list2 = input("enter a nested list e.g[[1,2],[1,2]]: ")
nested_list2 = ast.literal_eval(list2)
print("entered data: {nested_list2}")

rows2 = len(nested_list2)
columns2 = len(nested_list2[0])

if rows2 == columns2:
    for m in range(0, rows2):
        for n in range(0, columns2):
            if m + n == (rows2-1):
                print(nested_list2[m][n], end = " ")
            else:
                print("*", end = " ")
        print()