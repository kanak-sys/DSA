"create a dictionary for student"
"including keys like name, age, city, marks"
"print each piece of information using its key"


student = {"Name": "Kanak",
           "Age": 23,
           "City": "Dumka",
           "Marks": 98}
for each in student.keys():
    print(f"key: {each}, data: {student[each]}")