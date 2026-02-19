n = int(input("enter no of elements: "))
arr = []
for i in range(n):
    arr.append(int(input("enter elements: ")))

copy_arr = arr.copy()
print("original array: ", arr)
print("copy of array: ", copy_arr)