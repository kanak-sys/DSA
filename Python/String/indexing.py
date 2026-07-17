"POSITIVE INDEXING +ve"
"Left to Right"
name = "programming"
#       012345678910
print(name[0])
print(name[7])
print(name[5])

"NEGATIVE INDEXING -ve"
"Right to Left"
#       -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(name[-1])
print(name[-9])
print(name[-6])

"Slicing Powerful Technique"
"Allows u to extract portion or part of a string"

"BASIC SLICING"
print(name[0:5])
print(name[3:8])
print(name[:4])
print(name[10:4:-1])
print(name[7::-2])
print(name[5:])
print(name[::2])
print(name[::-1])

email = "mkanak0430@gmail.com"
username = email[:email.index("@")]
username2 = email[email.index("@")+1:]
print(username, username2)
