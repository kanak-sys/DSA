"""
reuseable block of code that performs specific tasks
instead of writing the same logic again and again
you write it once inside a function and 
call it whenever u need it
follows (dry- don't repeat yourself) principle
makes code
easier to read
easier to debug
easier to maintain

"""

#without function use
print("welcome, Rahul")
print("you have 3 new messages")
print("welcome, kanak")
print("you have 3 new messages")

def greet(name):                        #get registered in memory
    print(f"welcome, {name}")
    print("you have 3 new messages")
greet("Rahul")                          #calling a function
greet("kanak")

"""
you define a function using def keyword
def function_name():
    ----code----
function_name()"""