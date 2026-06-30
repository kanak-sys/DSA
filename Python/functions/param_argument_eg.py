"""
take 3 inputs from user
AS SUBJECT marks calulate their total and print average

"""

def calculate(sub1, sub2, sub3):
    total = sub1 + sub2 + sub3
    average = total / 3
    print(f"the total marks obtained: {average}")

calculate(45, 67, 98)

"""
ask name age gender
and print

"""
def query(name, age, gender):
    print(f"mr/mrs/miss {name}, of age {age} and gender {gender} is our guest")
n = input("enter guest name: ")
a = int(input("enter age: "))
g =input("enter gender: ")
query(n, a, g)
