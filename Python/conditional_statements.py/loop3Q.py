"""
#start to end print even numbers
"""

start = int(input("enter start no. "))
end = int(input("enter end number: "))
i = start
while i <= end:
    if i % 2 == 0:
        print(f"values :{i}")
    i += 1

    #---i += 1 -----if increament is shifted by tab  then infinite loops
    #runs as because if k andar i += 1 h so if is never true suppose 3 % 2 != 0 
    #then again i = 3 only cause i += 1 is inside if block

    