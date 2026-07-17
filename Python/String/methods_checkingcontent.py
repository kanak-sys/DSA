"methods that returns boolean values"
"based on content and charaacteristics of string"
#isalpha() - all letters(returns true if all characters in the strings are alphabetic & not empty)
#isdigit() - All digits(returns true if all characters in the string are digits & not empty)
#isalnum() - Alphanumeric only(returns True) if all characters(alphabetic or numbers only)
#isspace() - all whitespace(all characters are spaces/blanks) & \n & \t
sentence ="Abvcfyjm"
print(sentence.isalpha())

print("123456977".isdigit())

Alpno = "guy67gbhgyu6423"
res = Alpno.isalnum()
print(res)

Blank = "    \n\t  "
print(Blank.isspace())

"checking prefix and suffix"
"if it begins with or ends with specific characters"
#startswith("...")
#endswith("...")

filename ="Document_report.pdf"
print(filename.startswith("Document"))
print(filename.endswith(".pdf"))
print(filename.endswith(".jsx"))