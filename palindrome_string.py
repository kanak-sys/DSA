s = input("Enter a string: ")
rev = s[::-1]  # slicing method
if s == rev:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
#rev = " "
#for i in s:
#    rev = s[i] + rev
#if s == rev:
#    print("The string is a palindrome.")

#rev = ""
#for i in range(len(s)-1, -1, -1):
#    rev = rev + s[i]
#if s == rev:

#left = 0
#right = len(s) - 1
#while left < right:
#    if s[left] != s[right]:
#        print("The string is not a palindrome.")
#        break
#    left += 1
#    right -= 1
#else:
#    print("The string is a palindrome.")