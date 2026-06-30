#SCOPE - refers to where a variable is accessible in your code

"""
local -
A variable creared inside a function 
scope only exists inside that function

global - 
variable created outside all functions
can be accessed from anywhere.

"""

name = "kanak"      #global variable
def greet():
    message = "hello!!"     #local variable
    print(f"{message}, {name}")         #can read global variable
greet()
#print(message) #---> error can't read outside scope

"""
***
if u want to modify global variable
from inside a function
you must explicitly tell Python
using global keyword
***
"""
#
def greet(n1, n2):
    n1 = 100        #local
    n2 = 200        #local
    print(f"n1 - {n1} and n2 - {n2}")

n1 = 10             #global
n2 = 20             #global
greet(n1, n2)  
print(n1)
print(n2)