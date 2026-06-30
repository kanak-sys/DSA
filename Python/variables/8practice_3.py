"""
take the user age as input.
check and print whether they are eligible to vote (age >= 18) and 
whether they are a senior citizen(age >= 60)
print both result.
"""
age = int(input("enter your age:..."))
if age < 18:
    print("not eligible to vote")
else:
    print("eligible to vote")
if age >= 60:
    print("senior citizen") 