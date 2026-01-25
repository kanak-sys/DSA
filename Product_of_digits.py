num = int(input("Enter a number:"))
product_d = 1
while num > 0:
    digits = num % 10
    product_d = product_d * digits
    num = num // 10
print(" the product of digits: ", product_d)