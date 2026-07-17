"powerful data structure in python where the values of a dictionary are themselves dictionary"
"allows you to store complex hierarical data"

students = {"101":{"Name":"Archie", "Age": 34, "City": "Chattisgarh"},
            "102":{"Name":"Bob", "Age": 32, "City": "Ranchi"},
            "103":{"Name":"Charlie", "Age": 31, "City": "Kolkata"}
            }
#accesing nested dictionary
print(students["101"]["Name"])
print(students["103"]["Age"])

#adding new student
students["104"] = {"Name": "dev", "Age": 32, "City": "Noida"}

#updating
students["101"]["City"] = "Banglore"

print(students)

#Looping through nested dictionary
for rollNo, Info in students.items():
    print(f"Roll {rollNo}: {Info['Name']} from {Info['City']}")