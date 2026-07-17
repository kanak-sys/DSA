"Given a dictionary of marks for different subjects"
"loop over its values to calculate"
"and print total marks and the average marks obtained"

Marks = {"maths": 98,
         "english": 76,
         "physics": 89,
         "hindi": 73,
         "chemistry": 92}
n = len(Marks)
total = 0
for subject, mark in Marks.items():
    print(f"Subject & Marks Obtained: {subject},{mark}")
    total += mark
print(f"Total Marks: {total}")
average = total//n
print(f"Average: {average}")