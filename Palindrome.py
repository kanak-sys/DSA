def isPalindrome(s):
    original = s
    rev = 0
    while s>0:
        digit = s%10
        rev = rev * 10 + digit
        s = s//10
    return original == rev
n = int(input("Enter a number:" ))
if isPalindrome(n):
    print("The number is a palindrome")
else:
    print("the number is not a palindrome")