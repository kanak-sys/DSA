arr1 = list(map(int, input("enter elements of first array: ").split()))
arr2 = list(map(int, input("enter elements of second array: ").split()))
#merged_arr = arr1 + arr2 -- built in does not work for sorted arrays
#using loop
for i in arr2:
    arr1.append(i) 
    
print("merged array: ", arr1)