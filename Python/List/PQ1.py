"""
find the largest element.
Given a list of numbers, 
write a python code using a loop
to find and print
thelargest element in the list.

numbers = [10, 7, 34, 20, 4, 45, 86, 2, 90, 51, 1, 99]
expected output: 99

"""
numbers = [10, 7, -34, 20, -4, 45, 86, 2, -90, 51, 1, 99]
largest = float("-inf")  
for num in numbers:
    if num > largest:
        largest = num
print(f"maximum element is: {largest}")