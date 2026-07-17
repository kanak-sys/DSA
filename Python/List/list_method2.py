"""
powerful methods for organising and manipulating lists in Python
modify list in place
and provide information about its element
"""

#.sort()
"""sorts the elements of the list in ascending order directly
modifying the original list"""

nums = [ 3, 8, 2, 56, 83,45, 24, 91, 4, 98, 3]
nums.sort()
print(nums)

#.sort(reverse = True)
"""sorts the elements of the list in descending order
by setting the reverse parameter to True
"""

nums2 = [ 4, 87, 91, 47, 29, 4, 89, 91, 12, 7]
nums2.sort(reverse = True)
print(nums2)

#.reverse()
"""reverse the order of element in the list directly"""

nums3 = [ 7, 19, 13, 15, 21, 23, 9, 11, 17, 25]
nums3.reverse()
print(nums3)

#.index()
"""returns the index of first occurence of a specified value in list"""

fruits = ['mango', 'apple', 'kiwi', 'banana', 'orange']
print(fruits.index('kiwi'))

#.count()
"""Returns the number of times a specified value returns in a list"""

num = [2, 5, 6, 1, 8, 1, 2, 1, 1, 2, 3, 8, 1, 7]
print(num.count(1))
