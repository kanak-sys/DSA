n = int(input(" enter no of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(" enter element: ")))
unique_arr = []
for i in arr:
    if i not in unique_arr:
        unique_arr.append(i)
print("array with duplicates removed: ", unique_arr)