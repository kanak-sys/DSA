#creating String
name = "Kanak"
city = 'Delhi'
message = """This is a 
multi-line string"""

#printing string
print(name)
print(f"Hello, {name} from {city},{message}")

#string can contain any character
check = "@#.87hey"
print(check)

#strings are immutable
"once string objct is created"
"you cannn't change its individual character directly"
name = name[:1] + "ahul" 
print(name)

#indexing is possible
Name = "Kanak Mishra"
print(Name[0])
print(Name[-1])
print(Name[6])

#U CAN'T UPDATE STRING
#print Name[0] = "z"    ERROR- SHOWS STRINGS ARE IMMUTABLE

#U CAN OVERRIDE
Name = "CHANGE"
print(Name)