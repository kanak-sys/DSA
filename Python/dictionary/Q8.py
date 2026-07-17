"Subjects and Marks"
"create a dictionary of 6 subjects and their respective marks"
"print the subject with the highest marks"
"and the one with the lowest using max() and min() function "
"alongside a lambda expression"

subjects = {"Maths": 87, "Hindi": 68, "English": 98, "Computer": 78, "Science": 91, "Physical education": 76}
#fetching only values
highest_marks = max(subjects.values())
lowest_marks= min(subjects.values())

highest_sub = max(subjects, key = lambda x:subjects[x])
print("Highest Marks:")
print(highest_sub, ":" ,subjects[highest_sub])
lowest_sub = min(subjects, key = lambda x:subjects[x])
print("Lowest Marks:")
print(lowest_sub, ":" ,subjects[lowest_sub])
print(highest_marks, lowest_marks)