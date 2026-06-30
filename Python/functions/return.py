"""
sends
a value back
to whoever called the function

***note***
once python hits return statement. the function stops immediately
any code after return inside the function will never run
"""
#without return - does something but gives nothing back
def add(a, b):
    print(a + b)

# ------- result is lost -------

#with return - result can be stored and used
def add(a, b):
    return a + b
    print("hii")  #this line never runs

# ------- result can be stored and used -------

result = add(10, 5)
print(result)
print(add(7, 3) * 10) #runs with return

def can_vote(age):
    if age >= 18:
        return True
    else:
        return False
oky = can_vote(12)
print(oky)