n = int(input("enter the no of elements to b entered:"))
arr = list(map(int, input("enter the elements:").split()))
arr = arr[-1:] + arr[:-1]
#right rotation by 1
#arr = arr[1:] + arr[:1]
#left rotation by 1
print("the rotated array is:", arr)