"BUILT IN FUNCTIONS IN STRING"
#LEN()- returns a total no of character in string including spaces and special character
sentence = "welcomeinpythonprogramming"
n = len(sentence)
print(n)

#min() and max()- returns alphabetically smallest and largest character in string
mini = min(sentence)
maxi = max(sentence)
print(mini, ord(mini))
print(maxi)

#sorted- returns a new list containning all the items from string in ascending order
sort = sorted(sentence)
print(sort)
