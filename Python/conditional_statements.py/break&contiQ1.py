"""
take numbers as input from the user one by one.
skip negative numbers and keep adding the positive ones.
stop when the user enter 0 and print the total.
(uses both continue and break)
"""
total = 0
while True:
    num = int(input("enter no. - "))
    if num == 0:
        break
    if num < 0:
        continue
    total += num
print(f"Total: {total}")