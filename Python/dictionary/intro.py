"unordered collection of data values"
"used to store values in data - value pairs"

"think it as a real world dictionary where you look for a word(key) to find its meaning(value)"
"phone book where name(key) leads you to phone number(value)"


#empty dictionary
marks1 = {}
print(marks1, type(marks1))

#with data
marks2 = {"maths": 89, "english": 90, "hindi": 91, "science": 92}
print(marks2)

#allowed - tuple is immutable
marks3 = {"maths": 98, 55: "anirudh", 99: 76, "abc": [1, 2, 3], (1, 2, 4): "wfh"}
print(marks3)

#not allowed- keys must be immutable data type
"""marks4 = {[1, 3, 5]: "ritu"}
print(marks4)"""  #list are mutable



#keyvaluepair  

#mutable - dictionary are dynamic

#uniquekeys - each key within a dictionary must be unique, duplicate keys will simply overwrite previous entries

#immutable keys - list cannt be a key