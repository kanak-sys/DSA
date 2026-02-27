n = int(input("enter the size of array :"))
arr = list(map(int, input("enter the elements: ").split()))
count = 0
for i in arr:
    if i > 0:
        count += 1
print("the count of +ve numbers in the array is:", count)