n = int(input("enter the size of array  "))
arr = list(map(int, input("enter the elements: ").split()))
j = 0
for i in range(n):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1
print("the array after moving zeroes to end is:", arr)