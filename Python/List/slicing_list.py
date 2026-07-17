"""
Powerful feature:
allows you to extract a specific portion or "slice" from a list.
doesn't modify the original list
returns a new list containing the selected elements.

syntax: List_name[start:stop:step]:
start: The index where the slice starts (inclusive).
stop: The index where the slice ends (exclusive).
step: The step size or stride between elements in the slice. (optional) by default it is 1

for -ve step: right to left 
for +ve step: left to right

    -5 -4  -3  -2  -1
    0  1   2   3   4
    9  10  20  30  40  
    [::-1]
    start = 40
    stop = 9
    [::1]
    start = 9
    stop = 40
    

Example of list slicing:

"""

nums = [10, 20, 30, 43, 50, 60, 70, 80, 90, 100]
print(nums[1:5])
print(nums[:4])
print(nums[4:])
print(nums[::2])
print(nums[1:8:3])
print(nums[::-1])  # Reversing the list using slicing
print(nums[::-2])
print(nums[3:88]) #no error, but it will return elements from index 3 to the end of the list since 88 exceeds the list length.
print(nums[5:5]) #empty list or blank list
print(nums[0::3]) 
print(nums[9:3:-1])
print(nums[5::-1]) 