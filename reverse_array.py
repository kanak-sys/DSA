n = int(input("enter the number of elements "))
arr = []

for i in range(n):
    arr.append(int(input("enter element: ")))

rev = []
for i in range(n-1, -1, -1):
    rev.append(arr[i])

print("reversed array is: ", rev)