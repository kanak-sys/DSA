"""
if it is raining carry a umbrella otherwise don't

makes decisions based on conditions


1. if statement-
    condition is true the indented block runs
    if false it skips
    
2. if else statement-
3. if elif else statement-
    when you have multiple outcomes
    checks conditions from top to bottom
    runs the first one that is true and skips the rest
4. nested if statement-
     placing if statements inside another if statement
5. short hand if statement-

    """

marks = 45
if marks >= 30:
    print("if block executed")
else:
    print("else block executed")

stud_marks = int(input("enter your total marks: "))
if stud_marks >= 90 and stud_marks <= 100:
    print("grade A")
elif stud_marks >= 80 and stud_marks < 90:
    print("grade B")
elif stud_marks >= 70:
    print("grade C")
elif stud_marks >= 60:
    print("grade D")
elif stud_marks > 0 and stud_marks < 60:
    print("grade very bad")
else:
    print("invalid marks")

age = 45
certificate = True
if age >= 18:
    if certificate:
        print("can hire eligible")
else:
    print("can't hire not eligible")


status = "eligible" if age >= 18 else "not eligible"

print(f"your status is: {status}")
