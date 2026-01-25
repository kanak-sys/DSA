num = int(input("enter a number"))
count = 0
if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num = num // 10
print("the number of digits" , count)
