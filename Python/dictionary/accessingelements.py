name = {"neha": 9, "ritu": 10, "kavya": 11, "zaid": 12}
print(name["ritu"])
#print(name["abc"])         #key error

#using method 'get' to access
print(name.get("ritu"))
print(name.get("abc"))      #prints none
print(name.get("abc", 0))   #print 0 as default value is set to None
print(name.get("abc", -1))  #print -1 as default

subject = "ritu"
ans = name.get(subject)
if ans == None:
    print("Not Found")
else:
    print(f"marks scored = {ans}")