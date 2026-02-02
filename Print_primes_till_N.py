num = int(input("enter a number "))
for s in range(2, num+1):
    for i in range(2, int(s ** 0.5) + 1):
        if s % i == 0:
            break

    else:
        print(s , end="")