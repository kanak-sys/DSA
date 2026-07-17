"collection of values in a single variable similar to list"
"()"
"tuple is immutable, once created u can't change"
"you can't add or remove its elements"

cities_tuple = ("srinagar", "punjab", "rishikesh", 1, 2, 3)
#cities_tuple[0] = "chennai"     #typeerror
print(cities_tuple)
print(type(cities_tuple))

#items stay in the order you put them
#allows duplicate as same value can appear more than once
#cannot be modified after creation
#can hold any datatype, integers, float, string, boolean
#slightly faster
#less memory

"use when u want to protect data from accidental modification"


"only 2 methods available count and index same as done on list"

print(cities_tuple.count(1))
print(cities_tuple.index("punjab"))

