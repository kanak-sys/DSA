"Top 3 subjects by Marks"
"Given a dictionary of subjects and their marks"
"sorted in decending order then print only"
"the top 3 subjects"

subjects = {"Maths": 87, 
            "Hindi": 68, 
            "English": 98, 
            "Computer": 78, 
            "Science": 91, 
            "Physical education": 76
            }
ans = sorted(subjects.items(), key = lambda x: x[1], reverse= True)
result = ans[0:3]
for subject, mark in result:
    print(subject, mark)