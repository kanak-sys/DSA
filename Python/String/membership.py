"Membership check"
sentence = "Welcome in python programming"
print("p" in sentence)
print("z" in sentence)
print("python" in sentence)
print("java" in sentence)
print("to" not in sentence)

email = input("Enter your mail: ")
if "@" in email and "." in email:
    print("Looks like a valid address")
else:
    print("not a valid address")