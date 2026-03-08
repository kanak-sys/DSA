arr = list(map(int, input("enter elements: ").split()))
element = int(input("enter element to b inserted: "))
pos = int(input("enter position to insert element: "))

#arr.insert(pos, element)  - built in
#user-12 13   #insert-14   #pos-2  #out-[12 13 14]

arr.append(0)
for i in range(len(arr)-1, pos, -1):
    arr[i] = arr[i-1]
    arr[pos] = element
print("array after insertion: ", arr)
#user-12 13   #insert-14   #pos-2  #out-[12 13 0]
#user-12 13   #insert-14   #pos-1  #out-[12 14 13]