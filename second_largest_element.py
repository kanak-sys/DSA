n = int(input("enter no of elements: "))
arr = []

for i in range(n):
    arr.append(int(input("enter element and enter to add more: ")))
largest = second = -10**9

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("second largest element is: ", second)