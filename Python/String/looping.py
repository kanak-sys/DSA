name = "Kanak Mishra"
n = len(name)
for j in range(0, n):
    print(name[j])

for char in name:
    print(char, end = " ")
print()
i = 0
while i < len(name):
    print(name[i], end=" ")
    i += 1

for index,char in enumerate(name, start = 0):
    print(f"{index}:{char}")

sentence = "Welcome to python programming"
vowels = "aeiouAEIOU"
count = 0
for char in sentence:
    if char in vowels:
        count += 1
    print(f"Total Vowel: {count}")
