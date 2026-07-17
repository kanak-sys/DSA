"when working with complex data structure"
"that needs custom sorting"
"the sorted function becomes incredibly powerful when combined with lambda function"

"lambda s:s[keyname] instructs the sort functionto use values associated with the keyname"
"for each student dictionary "


students = {"101":{"Name":"Archie", "Age": 84, "City": "Chattisgarh"},
            "102":{"Name":"Bob", "Age": 32, "City": "Ranchi"},
            "103":{"Name":"Charlie", "Age": 11, "City": "Kolkata"},
            "104":{"Name": "dev", "Age": 62, "City": "Noida"}
            }

#sort by age(ascending)
by_age = sorted(students.items(), key = lambda s: s[1]["Age"])
print("Sorted by marks Ascending")
for s in by_age:
    print(s)

#sort by age(descending)
by_age_des = sorted(students.items(), key = lambda s: s[1]["Age"], reverse = True)
print(by_age_des)

#sort by name(alphabetically)
by_name = sorted(students.items(), key = lambda s: s[1]["Name"])
print(by_name)


#sort by its value
sorted_age = sorted(students.items(), key = lambda item:item[1]["Age"])
sorted_age_dict = dict(sorted_age)
print("Sorted by Values(ascending): ")
print(sorted_age_dict)

#sort by value descending
sorted_age_desc = sorted(students.items(), key = lambda item:item[1]["Age"], reverse=True)
sorted_age_desc_dict = dict(sorted_age_desc)
print(sorted_age_desc_dict)