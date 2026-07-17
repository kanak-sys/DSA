"Accessing Elements(Membership Check)"

fruits = {"Apple", "Banana", "Cherry"}
print("Apple" in fruits)
print("apple" in fruits)
print("Grapes" in fruits)
print("Kiwi" not in fruits)

allowed_users = {"rahul", "priya", "karan"}
user = input("enter username: ")
if user in allowed_users:
    print("Access Granted")
else:
    print("Access Denied")
    