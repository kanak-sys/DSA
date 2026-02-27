n = int(input("enter the size of array: "))
arr = list(map(int, input("enter the elements: ").split()))
k = int(input("enter the number of times to rotate: "))
k = k % n  # to handle cases where k > n
# right rotation by k
arr = arr[-k:] + arr[:-k]
# left rotation by k
# arr = arr[k:] + arr[:k]
print("the rotated array is:", arr)                 