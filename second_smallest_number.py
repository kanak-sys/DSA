n = int(input("enter no. of elements: "))
arr = []

for i in range(n):
    arr.append(int(input("enter element and enter to add more: ")))

smallest = second = 10**9

for num in arr:
    if num < smallest:
        second = smallest
        smallest = num
    elif num < second and num != smallest:
        second = num
print("second smallest element is: ", second)