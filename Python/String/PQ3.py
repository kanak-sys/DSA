"read a sentence from the user"
"count and print the total no of vowels"
"(a, e, i, o, u) case insensitive present in it"
"using a for loop"

sentence = input("Enter a Sentence: ")
count = 0
for ch in sentence:
    if ch in "aeiou":
        count += 1
print(count)