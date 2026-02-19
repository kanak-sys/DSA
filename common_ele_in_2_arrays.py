arr1 = list(map(int, input("enter elements of first array: ").split()))
arr2 = list(map(int, input("enter elements of second array: ").split()))
comm_arr = []
for i in arr1:
    if i in arr2 and i not in comm_arr:
        comm_arr.append(i)
print("common elements in both arrays: ", comm_arr)