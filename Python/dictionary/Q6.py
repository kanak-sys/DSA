"populate a dictionary with six student names and their corresponding marks"
"print the names of all students who acheived"
"a score above 75"

students = {"Alice":87,
            "bob":67,
            "charlie":78,
            "diana":76,
            "eve":67,
            "frank":98}
for name,marks in students.items():
    if marks >= 75:
        print(f" name: {name}")