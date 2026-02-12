n = int(input("enter a number :"))
if n > 0 and n % 10 == 0:
    while n % 10 == 0:
        n //= 10
    if n == 1:
        print("True")
    else:
        print("False") 
        
else: print("False")