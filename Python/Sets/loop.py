"Looping Through Sets"
"for loop"
fruits = {"Apple", "Banana", "Cherry"}
for fruit in fruits:
    print(fruit)

"Built In Functions FOR Sets"

nums = {40, 10, 90, 70, 30, 60, 20, 50, 80}
n= len(nums)
mini = min(nums)
maxi = max(nums)
total = sum(nums)
sort = sorted(nums)
decen_sort = sorted(nums, reverse= True)
print(f"Length: {n}",end =" ")
print(f"Minimum: {mini}",end = " ")
print(f"Maximum: {maxi}",end = " ")
print(f"Total Sum: {total}",end = " ") 
print(f"Sorted set: {sort}",end = " ")
print(f"Descending Order: {decen_sort}")