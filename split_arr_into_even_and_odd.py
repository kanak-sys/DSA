arr = list(map(int, input("enter elements: ").split()))
even_arr = []
odd_arr = []

for i in arr:
    if i % 2 == 0:
        even_arr.append(i)
    else:
        odd_arr.append(i)

print("even numbers:", even_arr)
print("odd numbers:", odd_arr)  