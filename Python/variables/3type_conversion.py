"""
implicit type of conversion
1. int to float
python does it automatically
"""
x = 5
y = 10.0
z = x + y
print(x)
print(y)
print(z)
print(type(z))

"""
explicit type of conversion
1. str to int


"""
num1 = "500"
num2 = "200"

print(num1 + num2) # it will concatenate the two strings and give 500200

num3 = int(num1)
num4 = int(num2)

print(int(num1) + int(num2))
print(num3 + num4) # it will add the two numbers and give 700


a= 500.1
b= 500.9
print(int(a)) # it will convert float to int and give 500
print(int(b)) # it will convert float to int and give 500