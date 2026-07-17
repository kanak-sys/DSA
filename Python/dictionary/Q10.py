"Students Details"
"create a nested dictionary"
"containing details of 4 student"
"where each student entry includes their name, age, city"
"write a loop to print the full details of each students"
"in clear, readable format"

students = {"Stud1":{"Name":"Archie", "Age":78, "City":"Ahmedabad"},
            "Stud2":{"Name":"Bob", "Age":56, "City":"Banke"},
            "Stud3":{"Name":"Charlie", "Age":91, "City":"Chattisgarh"},
            "Stud4":{"Name":"Dev", "Age":66, "City":"Delhi"}}
for studNo, Info in students.items():
    print(f"Student No. {studNo}:{Info['Name']} of {Info['Age']} years old from {Info['City']}")