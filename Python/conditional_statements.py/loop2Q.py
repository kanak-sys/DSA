"""
start to end by user
print using while loop
"""
start = int(input("enter start no. "))  # 5
end = int(input("enter end number: ")) # 11
while start <= end:
    print(f"value : {start}")
    start += 1

print(f" after loop start value is {start}")   #hence made changes in user entered value

#-------instead---------------------------

start = int(input("enter start no. "))
end = int(input("enter end number: "))
i = start
while i <= end:
    print(f"values :{i}")
    i += 1
print(f" start value after loop {start}")

