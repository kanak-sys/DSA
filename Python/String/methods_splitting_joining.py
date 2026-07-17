"split() - break string into list"
"by default it splits the string by whitespaces/blanks"
"you can also specify a custom delimitter"
"returns error it after splitting you print the desired list index and that index is not aavailable"

sentence = "python is fun and powerful"
#default(spaces)
words = sentence.split()
print(words)

#split by specific character like , @ # . etc
csv = "apple,mango,banana,cherry,pineapple,orange"
words2 = csv.split(",")
print(words2)
print(words2[2])
print(words2[5])

"join()- combine list into string"
"concatenate element of an iterable into an string"
"the string on which join is called "
"acts as a separator between the elements"

words = ["python", "is", "powerful"]
#join with space as separator
line = " ".join(words)
print(line)

#join with - as separator
line2 = "-".join(words)
print(line2)

#join with no separator
line3 = "".join(words)
print(line3)

#practical use:- formatting a shooping list
items = ["breads", "milk", "egg", "butter"]
print("shopping list: " + ",".join(items))

#how to join int into list
#we know string can join into list
#and if we typecast int into str during for loop
my_list = ['k', 'a', 'n', 'a', 'k', 5]
ans = "".join(str(ch) for ch in my_list)
print(ans)
print(type(ans))
