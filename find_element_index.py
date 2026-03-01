#n = int(input(" Enter no. of elements in list: "))
arr = list(map(int, input("enter elements").split()))
x = int(input("enter element to find its index:"))

if x in arr:
    print("index of element is", arr.index(x))
else:
    print("element not found")