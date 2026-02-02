num = int(input("enter a number "))
temp = num
digits = len(str(num))
sumV = 0
while temp > 0:
    digitC = temp % 10
    sumV += digitC ** digits
    temp //= 10
if sumV == num:
    print("armstrong number")
else:
    print("not a armstrong number153")