n = int(input("enter a no. of elements in list: "))
arr = list(map(int, input("enter elements").split()))

for i in range(n):
    if arr[i] % 2 ==0:
        arr[i] = 0
print(arr)