"""find the largest and smallest number,
in a list without using built-in functions like max() or min()
use a loop and a variable
to track the current largest/smallest as u go through the list.
"""

numbers = [10, 7, -34, 20, -4, 45, 86, 2, -90, 51, 1, 99]
largest = float("-inf")  
smallest = float("inf")
for num in numbers:
    if num > largest:
        largest = num
for nums in numbers:
    if nums < smallest:
        smallest = nums
print(f"maximum element is: {largest}")
print(f"minimum element is: {smallest}")
