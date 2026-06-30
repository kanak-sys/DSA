"""
also called keyword argument

let you pass values to a function
by explicitly nameing the parameter

means u can pass them in any order
u r no longer dependent on position
"""
def introduce(name, age, city):
    print(f"{name} is {age} years old, from {city}")

#positional orders matters
introduce("kanak", 22, "delhi")

#keyword orders doesn't matters
introduce(age = 21, name = "tisha", city = "mumbai")
introduce(city = "delhi", name = "palak", age = 19)