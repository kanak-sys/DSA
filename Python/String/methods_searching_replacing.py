"to locate substring, count their occurence and replace them"
"are essential for text processing, data manipulation and input validation"
#count = substring(Frequency)
#returns the number of non-overlapping occurence of substring in string
#if not found return 0

sentence = "python is great and python is powerful"
print(sentence.count("python"))
print(sentence.count("java"))

#find- locate first occurence
#returns the lowest index in a string where the substring is found
#if not found returns -1

print(sentence.find("python"))
print(sentence.find("great"))
print(sentence.find("java"))

#index(): locate with error
#similar to find but
#raises a ValueError if string is not found

print(sentence.index("python"))
#print(sentence.index("java"))      --------------- ERROR

#replace - substitute substring
#returns a new string
#with all occurences of an old substring replaces by a new one
#an optional third argument specifies the maximum number of replacements

print(sentence.replace("python", "java"))
print(sentence.replace("python", "java", 1))
