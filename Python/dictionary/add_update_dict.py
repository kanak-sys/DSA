student = {"name": "rahul", "age": 22}

#adding dictionary_name["new key that doesn't exist"] = any value
student["city"] = "delhi"
student["marks"] = 85
print(student)

#updating
student . update({"phone":902304,
                  "state":"gujrat",
                  "age":40})

#updating dictionary_name["key"] = new value 
student["age"] = 21
student["city"] = "mumbai"
print(student)

#Removing
removed = student.pop("marks")
print(f"Removed Value: {removed}")
print(f"dictionary after pop: {student}")

#pop with default
value = student.pop("grade", "not found")
print(f"attempt to pop non-exitence key: {value}")

#delete keyword
del student["city"]
print(f"dictionary after delete: {student}")

#empty the dictory - clear
student.clear()