"""
a student who scored marks in 3 subjects. take all 3 as input,
calculate the total and average, and print both using a f string
"""
sub1 = int(input("enter marks of subject 1:"))
sub2 = int(input("enter marks of subject 2:"))
sub3 = int(input("enter marks of subject 3:"))
total = sub1 + sub2 + sub3
average = total/3
print(f"total marks: {total} and average marks: {average:.2f}")
