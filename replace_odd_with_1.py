arr = list(map(int, input("enter elements: ").split()))
for i in range(len(arr)):
    if arr[i] % 2 != 0:
        arr[i] = 1
print(arr)