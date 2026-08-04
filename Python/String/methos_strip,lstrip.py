"methods crucial for data cleaning"
"allow you to remove unwanted whitespaces"
"and specified characters from the beginning "
"end or anywhere"

#strip - removes leading/trailing
#removes all whitespaces characters tabs, newlines
#from both ends of string
#original string remains unchanged
pythontext = "     Hellowold    "
ans = pythontext.strip()
print(ans)

#lstrip - removes all whitespaces
#character spaces from the left end of string

ans2 = pythontext.lstrip()
print(ans2)

#rstrip() - removes all whitespaces from the right end of string
ans3 = pythontext.rstrip()
print(ans3)
