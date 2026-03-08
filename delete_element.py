arr = list(map(int, input("enter elements: ").split()))
pos = int(input("enter position to delete element: "))
#arr.pop(pos) - built in

for i in range(pos, len(arr)-1):
    arr[i] = arr[i+1]
print("array after deletion: ", arr[:-1])

#print("array after deletion: ", arr)