"take a sentence from user and print it reversing words"
#python is good ...... good is python

sentence = input("Enter prompt: ")
word_list = sentence.split()
print(word_list)
reverse_list = word_list[::-1]
print(reverse_list)
ans = " ".join(reverse_list)
print(ans)