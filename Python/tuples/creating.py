#empty tuple
empty = ()

#tuple of integers
marks = ("12", "23", "34", "45", "56")

#tuple of strings
cities = ("delhi", "dumka", "dhanbad", "mumbai", "jharkhand")
#itrations
n = len(cities)
for i in range(0, n):
    print(cities[i], end = " ")
print()

for city in cities:
    print(city, end = " ")
print()
for index, value in enumerate(cities):
    print(f" index = {index}, value = {value}")

#tuples containning all
mixed = ("hey", 2, "o", True)

#accesing elements
print(cities[0])
print(marks[3])

print(mixed[-1])
print(marks[-3])

#slicing elements
print(marks[1:4])
print(cities[:3])
print(cities[4:])
print(marks[::2])
x = mixed[::-1]
print(x)
print(mixed)

#immutability results typeerror
#mixed.append("purple")
#del cities[1]

#tuple itself is immutable, it can contain reference to mutable objects
python_data = ("rahul", 21, [54, 85, 23])
#python_data[2] = [100, 100, 100] #typeerror
python_data[2].append(67)
print(python_data)

