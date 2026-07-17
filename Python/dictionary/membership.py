student = {'name': 'rahul', 'age': 21, 'city': 'mumbai', 'marks': 85, 'phone': 902304, 'state': 'gujrat'}

#checking if key exists returns true or false
#only check for keys not values

print('name' in student)
print("age" not in student)

if 'grade' not in student:
    student["grade"] = "unknown"
print(student)

k = input("enter key: ")
if k in student:
    print(student[k])
else:
    print("key doesnot exist")