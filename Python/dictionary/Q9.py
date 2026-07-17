"Student marks analysis"
"design a dictionary where each key is a student's name"
"and the corresponding value is a list of their marks in 3 different subjects"
"calculate and print"
"total marks and average marks for each students"

Students = {"Alice":[78, 92, 86],
            "Bob":[62, 54, 48],
            "Charlie":[98, 99, 96], 
            "Diana":[12, 9, 26], 
            "Ethane":[67, 86, 72]
            }
total = 0
for name, mark in Students.items():
    total = sum(mark)
    average = total / len(mark)
    print(f"{name}, has scored a total of {total} & average of {average:.2f} marks")
