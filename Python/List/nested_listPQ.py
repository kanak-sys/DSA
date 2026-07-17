"take a nested list from user and"
"check if the given matrix is a sqaure matrix, "
"print its lower triangle as it is "
"replace its upper triangle with '*' "

import ast
list = input("enter a nested list e.g[[1,2],[2,3]]: ")
nested_list = ast.literal_eval(list)
print(nested_list)

rows = len(nested_list)
columns = len(nested_list[0])
if rows == columns:
    print(f"its a square matrix")
    for i in range(0, rows):
        for j in range(0, columns):
            if i >= j:
                print(nested_list[i][j], end = " ")
            else:
                print("*", end = " ")
        print()
