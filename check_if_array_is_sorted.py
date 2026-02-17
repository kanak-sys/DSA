n = int(input("enter no of elements: "))
arr = []

for i in range(n):
    arr.append(int(input("enter elements: ")))

flag = True

for i in range(n-1):
    if arr[i] > arr[i+1]:
        flag = False
        break
if flag:
    print("array is sorted")
else:
    print("array is not sorted")
