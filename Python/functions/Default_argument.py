"""
value that a parameter takes automatically
if no argument is passed
when calling the function
makes certain parameters optional


parameters with default values
#def greet(name, message = "good morning"):  ->->-> CORRECT
must always come after
parameters without default values
#def greet(message = "good morning", name):  ->->-> WRONG

"""

def greet(name, message = "good morning"):
    print(f"{name}, {message}!")
greet("kanak")
greet("kanak", "good night")
